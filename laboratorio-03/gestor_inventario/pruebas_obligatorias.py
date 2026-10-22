"""Pruebas obligatorias del Laboratorio 3 (sección 16 y 17 del enunciado).

Simulan al usuario reemplazando input() y comprueban lo que muestra main.py.
Ejecutar:  python pruebas_obligatorias.py
"""

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

import main
from inventario import Inventario
from producto import Producto


def ejecutar(entradas):
    """Ejecuta main.main() con entradas simuladas y devuelve lo impreso."""
    salida = io.StringIO()
    with patch("builtins.input", side_effect=entradas), redirect_stdout(salida):
        main.main()
    return salida.getvalue()


def registrar(codigo, nombre, categoria, precio, cantidad):
    return ["1", codigo, nombre, categoria, str(precio), str(cantidad)]


class PruebasObligatorias(unittest.TestCase):
    def test_01_inventario_vacio(self):
        texto = ejecutar(["2", "7", "0"])
        self.assertIn("El inventario está vacío.", texto)
        self.assertIn("Productos registrados: 0", texto)
        self.assertIn("Unidades disponibles: 0", texto)

    def test_02_registrar_p001(self):
        texto = ejecutar(registrar("P001", "Teclado", "Periféricos", 85000, 4) + ["0"])
        self.assertIn("Producto registrado.", texto)

    def test_03_codigo_repetido(self):
        entradas = (
            registrar("P001", "Teclado", "Periféricos", 85000, 4)
            + registrar("P001", "Otro", "Accesorios", 10, 1)
            + ["2", "0"]
        )
        texto = ejecutar(entradas)
        self.assertIn("el código ya existe", texto)
        self.assertNotIn("Otro", texto)

    def test_04_codigo_o_nombre_vacio(self):
        # leer_texto vuelve a pedir el dato; el registro parcial nunca se guarda.
        entradas = ["1", "", "   ", "P001", "", "Teclado", "Periféricos", "100", "1", "2", "0"]
        texto = ejecutar(entradas)
        self.assertIn("Este campo no puede estar vacío.", texto)
        self.assertIn("P001 - Teclado", texto)

    def test_05_categoria_no_permitida(self):
        texto = ejecutar(registrar("P001", "Teclado", "Juguetes", 100, 1) + ["2", "0"])
        self.assertIn("No se pudo registrar el producto", texto)
        self.assertIn("El inventario está vacío.", texto)

    def test_06_precio_cero_o_negativo(self):
        entradas = ["1", "P001", "Teclado", "Periféricos", "0", "-5", "100", "1", "2", "0"]
        texto = ejecutar(entradas)
        self.assertEqual(texto.count("El precio debe ser mayor que cero."), 2)
        self.assertIn("P001 - Teclado", texto)

    def test_07_cantidad_negativa(self):
        entradas = ["1", "P001", "Teclado", "Periféricos", "100", "-1", "3", "2", "0"]
        texto = ejecutar(entradas)
        self.assertIn("La cantidad no puede ser negativa.", texto)
        self.assertIn("3 unidades", texto)

    def test_08_cantidad_cero_es_valida(self):
        texto = ejecutar(registrar("P002", "Mouse", "Periféricos", 45000, 0) + ["6", "0"])
        self.assertIn("Producto registrado.", texto)
        self.assertIn("- Mouse", texto)

    def test_09_buscar_existente(self):
        entradas = registrar("P001", "Teclado", "Periféricos", 85000, 4) + ["3", "P001", "0"]
        texto = ejecutar(entradas)
        self.assertEqual(texto.count("P001 - Teclado - Periféricos - $85000.0 - 4 unidades"), 1)

    def test_10_buscar_inexistente(self):
        texto = ejecutar(["3", "P999", "0"])
        self.assertIn("Producto no registrado.", texto)

    def test_11_actualizar_a_10(self):
        entradas = registrar("P001", "Teclado", "Periféricos", 85000, 4) + ["4", "P001", "10", "2", "0"]
        texto = ejecutar(entradas)
        self.assertIn("Existencias actualizadas.", texto)
        self.assertIn("P001 - Teclado - Periféricos - $85000.0 - 10 unidades", texto)

    def test_12_actualizar_a_negativo_conserva_dato(self):
        entradas = registrar("P001", "Teclado", "Periféricos", 85000, 4) + ["4", "P001", "-3", "10", "2", "0"]
        texto = ejecutar(entradas)
        self.assertIn("La cantidad no puede ser negativa.", texto)
        producto = Producto("P001", "Teclado", "Periféricos", 85000, 4)
        self.assertFalse(producto.actualizar_existencias(-3))
        self.assertEqual(producto.cantidad, 4)

    def test_13_eliminar_existente(self):
        entradas = registrar("P001", "Teclado", "Periféricos", 85000, 4) + ["5", "P001", "2", "0"]
        texto = ejecutar(entradas)
        self.assertIn("Producto eliminado.", texto)
        self.assertIn("El inventario está vacío.", texto)

    def test_14_eliminar_inexistente_no_falla(self):
        texto = ejecutar(["5", "P999", "0"])
        self.assertIn("Producto no registrado; no se eliminó nada.", texto)

    def test_15_texto_en_campo_numerico(self):
        entradas = ["1", "P001", "Teclado", "Periféricos", "abc", "100", "xyz", "2", "2", "0"]
        texto = ejecutar(entradas)
        self.assertIn("Debes escribir un número válido.", texto)
        self.assertIn("Debes escribir un número entero.", texto)
        self.assertIn("P001 - Teclado", texto)

    def test_16_resumen_numerico_del_enunciado(self):
        entradas = (
            registrar("P001", "Teclado", "Periféricos", 85000, 4)
            + registrar("P002", "Mouse", "Periféricos", 45000, 0)
            + registrar("P003", "Monitor", "Componentes", 700000, 2)
            + ["7", "6", "4", "P002", "5", "7", "0"]
        )
        texto = ejecutar(entradas)
        self.assertIn("Productos registrados: 3", texto)
        self.assertIn("Unidades disponibles: 6", texto)
        self.assertIn("Valor del inventario: $1740000.0", texto)
        self.assertIn("Cantidad de categorías: 2", texto)
        self.assertIn("- Mouse", texto)
        self.assertIn("Unidades disponibles: 11", texto)
        self.assertIn("Valor del inventario: $1965000.0", texto)

    def test_17_salir_y_opcion_invalida(self):
        texto = ejecutar(["9", "0"])
        self.assertIn("Opción no válida.", texto)
        self.assertIn("Programa finalizado.", texto)

    def test_18_independencia_de_inventarios(self):
        primero, segundo = Inventario(), Inventario()
        primero.registrar_producto(Producto("P001", "Teclado", "Periféricos", 85000, 4))
        self.assertEqual(len(primero.listar_productos()), 1)
        self.assertEqual(len(segundo.listar_productos()), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
