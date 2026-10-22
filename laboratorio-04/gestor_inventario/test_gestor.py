import csv, json, math, tempfile, unittest
from pathlib import Path
from almacenamiento import ErrorAlmacenamiento, cargar_inventario, guardar_inventario
from inventario import Inventario
from producto import CATEGORIAS, Producto
from reportes import CAMPOS, exportar_csv

class PruebasInventarioPersistente(unittest.TestCase):
    def setUp(self): self.tmp = tempfile.TemporaryDirectory(); self.base = Path(self.tmp.name)
    def tearDown(self): self.tmp.cleanup()
    def muestra(self):
        inv = Inventario()
        for datos in [("P001", "Teclado", "Periféricos", 85000, 4),
                      ("P002", "Mouse", "Periféricos", 45000, 0),
                      ("P003", "Disco SSD", "Componentes", 700000, 2)]:
            self.assertTrue(inv.registrar_producto(Producto(*datos)))
        return inv
    def test_producto_validaciones_y_serializacion(self):
        p = Producto(" p001 ", " Teclado ", "Periféricos", 85000, 4)
        self.assertEqual(p.codigo, "P001")
        self.assertEqual(Producto.desde_diccionario(p.a_diccionario()).a_diccionario(), p.a_diccionario())
        for args in [("", "x", "Periféricos", 1, 0), ("a", "x", "Otro", 1, 0),
                     ("a", "x", "Periféricos", math.inf, 0), ("a", "x", "Periféricos", 1, -1)]:
            with self.assertRaises((ValueError, TypeError)): Producto(*args)
    def test_no_admite_duplicados_y_actualiza(self):
        inv = self.muestra(); self.assertFalse(inv.registrar_producto(Producto("P001", "Otro", "Accesorios", 10, 1)))
        self.assertFalse(inv.actualizar_existencias("P001", -1)); self.assertEqual(inv.buscar_producto("p001").cantidad, 4)
        self.assertTrue(inv.actualizar_existencias("P002", 5))
    def test_inventarios_independientes_y_lista_copia(self):
        a, b = self.muestra(), Inventario(); copia = a.listar_productos(); copia.clear()
        self.assertEqual(len(a.listar_productos()), 3); self.assertEqual(len(b.listar_productos()), 0)
    def test_resumen_y_agotados(self):
        inv = self.muestra(); r = inv.resumen()
        self.assertEqual((r["productos_registrados"], r["unidades_disponibles"], r["valor_total"]), (3, 6, 1740000))
        self.assertEqual([p.codigo for p in inv.productos_sin_stock()], ["P002"])
    def test_archivo_ausente_inicia_vacio(self):
        inv = cargar_inventario(self.base / "no-existe.json"); self.assertEqual(inv.listar_productos(), [])
    def test_guardar_recuperar_desde_directorio_distinto(self):
        ruta = self.base / "sub" / "productos.json"; original = self.muestra(); guardar_inventario(original, ruta)
        recuperado = cargar_inventario(ruta)
        self.assertEqual(recuperado.exportar_datos(), original.exportar_datos())
    def test_json_mal_formado_no_se_pisa(self):
        ruta = self.base / "malo.json"; original = '[{"sin": "coma"' ; ruta.write_text(original, encoding="utf-8")
        with self.assertRaises(ErrorAlmacenamiento): cargar_inventario(ruta)
        self.assertEqual(ruta.read_text(encoding="utf-8"), original)
    def test_registro_invalido_o_duplicado_rechaza_carga_completa(self):
        ruta = self.base / "invalido.json"
        for datos in [[{"codigo":"P1","nombre":"A","categoria":"Periféricos","precio":1,"cantidad":1},
                       {"codigo":"P1","nombre":"B","categoria":"Periféricos","precio":1,"cantidad":1}],
                      [{"codigo":"P1","nombre":"A","categoria":"NO","precio":1,"cantidad":1}]]:
            ruta.write_text(json.dumps(datos), encoding="utf-8")
            with self.assertRaises(ErrorAlmacenamiento): cargar_inventario(ruta)
    def test_csv_encabezados_y_valor(self):
        ruta = exportar_csv(self.muestra(), self.base / "reportes" / "inv.csv")
        with ruta.open(newline="", encoding="utf-8") as f: filas = list(csv.DictReader(f))
        self.assertEqual(list(filas[0]), CAMPOS); self.assertEqual(float(filas[0]["valor_inventario"]), 340000)
        self.assertEqual(float(filas[1]["valor_inventario"]), 0)
    def test_json_y_csv_son_separados(self):
        ruta = self.base / "inv.json"; inv = self.muestra(); guardar_inventario(inv, ruta)
        exportar_csv(inv, self.base / "inv.csv"); inv.actualizar_existencias("P002", 5)
        self.assertEqual(len(json.loads(ruta.read_text(encoding="utf-8"))), 3)
        self.assertEqual(cargar_inventario(ruta).buscar_producto("P002").cantidad, 0)

if __name__ == "__main__": unittest.main()
