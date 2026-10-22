"""Pruebas obligatorias del Laboratorio 4 (secciones 16, 17 y 18 del enunciado).

Simulan sesiones completas del menú con input() falso y un directorio temporal,
de modo que NUNCA tocan datos/productos.json real.
Ejecutar:  python pruebas_obligatorias.py
"""

import csv
import io
import json
import tempfile
import unittest
from contextlib import redirect_stdout
from functools import partial
from pathlib import Path
from unittest.mock import patch

import almacenamiento
import main
import reportes


def sesion(ruta_json, ruta_csv, entradas):
    """Equivale a abrir el programa, escribir `entradas` y cerrarlo."""
    salida = io.StringIO()
    with patch("builtins.input", side_effect=entradas), redirect_stdout(salida), \
         patch.object(main, "cargar_inventario", partial(almacenamiento.cargar_inventario, ruta_json)), \
         patch.object(main, "guardar_inventario", partial(almacenamiento.guardar_inventario, ruta=ruta_json)), \
         patch.object(main, "exportar_csv", partial(reportes.exportar_csv, ruta=ruta_csv)):
        main.main()
    return salida.getvalue()


def alta(codigo, nombre, categoria, precio, cantidad):
    return ["1", codigo, nombre, categoria, str(precio), str(cantidad)]


class PruebasObligatorias(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        base = Path(self.tmp.name)
        self.json = base / "datos" / "productos.json"
        self.csv = base / "reportes" / "inventario.csv"

    def tearDown(self):
        self.tmp.cleanup()

    def ejecutar(self, entradas):
        return sesion(self.json, self.csv, entradas)

    def tres_productos(self):
        return (alta("P001", "Teclado", "Periféricos", 85000, 4)
                + alta("P002", "Mouse", "Periféricos", 45000, 0)
                + alta("P003", "Monitor", "Componentes", 700000, 2))

    # 1
    def test_01_primera_ejecucion_sin_json(self):
        self.assertFalse(self.json.exists())
        texto = self.ejecutar(["2", "0"])
        self.assertIn("Productos recuperados: 0", texto)
        self.assertIn("No hay productos registrados.", texto)

    # 2 y 3
    def test_02_03_guardar_y_reiniciar(self):
        self.ejecutar(alta("P001", "Teclado", "Periféricos", 85000, 4)
                      + alta("P002", "Mouse", "Periféricos", 45000, 0) + ["0"])
        datos = json.loads(self.json.read_text(encoding="utf-8"))
        self.assertEqual([d["codigo"] for d in datos], ["P001", "P002"])
        texto = self.ejecutar(["2", "0"])
        self.assertIn("Productos recuperados: 2", texto)
        self.assertIn("P001 - Teclado", texto)
        self.assertIn("P002 - Mouse", texto)

    # 4
    def test_04_codigo_duplicado_no_duplica_json(self):
        self.ejecutar(alta("P001", "Teclado", "Periféricos", 85000, 4)
                      + alta("P001", "Otro", "Accesorios", 10, 1) + ["0"])
        self.assertEqual(len(json.loads(self.json.read_text(encoding="utf-8"))), 1)

    # 5
    def test_05_categoria_desconocida(self):
        texto = self.ejecutar(alta("P001", "X", "Juguetes", 10, 1) + ["2", "0"])
        self.assertIn("Datos rechazados", texto)
        self.assertIn("No hay productos registrados.", texto)

    # 6 y 7
    def test_06_07_precio_negativo_nan_inf(self):
        entradas = ["1", "P001", "X", "Periféricos", "-5", "nan", "inf", "abc", "100", "1", "0"]
        texto = self.ejecutar(entradas)
        self.assertEqual(texto.count("El precio debe ser finito y mayor que cero."), 3)
        self.assertIn("Escribe un precio válido", texto)
        self.assertEqual(json.loads(self.json.read_text(encoding="utf-8"))[0]["precio"], 100.0)

    # 8 y 9
    def test_08_09_cantidad_negativa_y_cero(self):
        entradas = ["1", "P001", "X", "Periféricos", "100", "-1", "hola", "0", "6", "0"]
        texto = self.ejecutar(entradas)
        self.assertIn("El valor debe ser como mínimo 0.", texto)
        self.assertIn("Escribe un número entero.", texto)
        self.assertIn("P001 - X", texto)  # aceptado como producto sin stock

    # 10
    def test_10_actualizar_persiste(self):
        self.ejecutar(alta("P002", "Mouse", "Periféricos", 45000, 0) + ["4", "P002", "5", "0"])
        texto = self.ejecutar(["3", "P002", "0"])
        self.assertIn("5 unidades", texto)

    # 11
    def test_11_eliminar_persiste(self):
        self.ejecutar(alta("P001", "A", "Periféricos", 10, 1) + ["5", "P001", "0"])
        texto = self.ejecutar(["2", "0"])
        self.assertIn("No hay productos registrados.", texto)

    # 12
    def test_12_texto_no_numerico(self):
        texto = self.ejecutar(["1", "P001", "X", "Periféricos", "abc", "100", "xyz", "2", "0"])
        self.assertIn("Escribe un precio válido", texto)
        self.assertIn("Escribe un número entero.", texto)

    # 13 (sección 18)
    def test_13_json_con_sintaxis_incorrecta(self):
        self.ejecutar(self.tres_productos() + ["0"])
        valido = self.json.read_text(encoding="utf-8")
        danado = valido.replace('},', '}', 1)  # se elimina una coma
        self.json.write_text(danado, encoding="utf-8")
        texto = self.ejecutar(alta("P009", "Nuevo", "Accesorios", 5, 1) + ["8", "0"])
        self.assertIn("No fue posible cargar el inventario", texto)
        self.assertIn("Operación bloqueada", texto)
        self.assertIn("Guardado bloqueado", texto)
        self.assertEqual(self.json.read_text(encoding="utf-8"), danado)  # no se pisó con []
        self.json.write_text(valido, encoding="utf-8")  # se restaura la copia válida
        self.assertIn("Productos recuperados: 3", self.ejecutar(["0"]))

    # 14
    def test_14_estructura_inesperada(self):
        self.json.parent.mkdir(parents=True)
        for contenido in ['{"codigo": "P001"}', '[1, 2]', '[{"codigo": "P001"}]']:
            self.json.write_text(contenido, encoding="utf-8")
            texto = self.ejecutar(["0"])
            self.assertIn("No fue posible cargar el inventario", texto)
            self.assertEqual(self.json.read_text(encoding="utf-8"), contenido)

    # 15
    def test_15_codigo_repetido_en_json_sin_carga_parcial(self):
        reg = {"codigo": "P1", "nombre": "A", "categoria": "Periféricos", "precio": 1, "cantidad": 1}
        self.json.parent.mkdir(parents=True)
        contenido = json.dumps([reg, dict(reg, nombre="B")])
        self.json.write_text(contenido, encoding="utf-8")
        texto = self.ejecutar(["2", "0"])
        self.assertIn("Código duplicado", texto)
        self.assertNotIn("P1 - A", texto)
        self.assertEqual(self.json.read_text(encoding="utf-8"), contenido)

    # 16
    def test_16_error_de_escritura_no_se_presenta_como_exito(self):
        entradas = alta("P001", "A", "Periféricos", 10, 1) + ["0"]
        salida = io.StringIO()
        with patch("builtins.input", side_effect=entradas), redirect_stdout(salida), \
             patch.object(main, "cargar_inventario", partial(almacenamiento.cargar_inventario, self.json)), \
             patch.object(main, "guardar_inventario", side_effect=OSError("disco lleno")):
            main.main()
        texto = salida.getvalue()
        self.assertIn("No se pudo guardar; el cambio queda solo en memoria", texto)
        self.assertNotIn("Guardado en:", texto)
        self.assertFalse(self.json.exists())

    # 17
    def test_17_exportar_csv(self):
        self.ejecutar(self.tres_productos() + ["4", "P002", "5", "9", "0"])
        with self.csv.open(newline="", encoding="utf-8") as f:
            filas = list(csv.DictReader(f))
        self.assertEqual(list(filas[0]), ["codigo", "nombre", "categoria", "precio", "cantidad", "valor_inventario"])
        valores = {f["codigo"]: float(f["valor_inventario"]) for f in filas}
        self.assertEqual(valores, {"P001": 340000.0, "P002": 225000.0, "P003": 1400000.0})

    # 18 y sección 17 (prueba numérica con reinicio)
    def test_18_resumen_y_prueba_numerica_con_reinicio(self):
        self.ejecutar(self.tres_productos() + ["0"])
        texto = self.ejecutar(["7", "6", "0"])
        self.assertIn("Productos registrados: 3", texto)
        self.assertIn("Unidades disponibles: 6", texto)
        self.assertIn("Valor del inventario: $1740000.0", texto)
        self.assertIn("Categorías utilizadas: 2", texto)
        self.assertIn("P002 - Mouse", texto)
        texto = self.ejecutar(["4", "P002", "5", "0"])
        texto = self.ejecutar(["7", "0"])
        self.assertIn("Unidades disponibles: 11", texto)
        self.assertIn("Valor del inventario: $1965000.0", texto)

    # 19
    def test_19_salida_controlada(self):
        self.assertIn("Programa finalizado.", self.ejecutar(["9", "0"]))


if __name__ == "__main__":
    unittest.main(verbosity=2)
