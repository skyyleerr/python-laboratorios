import unittest

from inventario import Inventario
from producto import CATEGORIAS, Producto
from main import convertir_precio


class PruebasProducto(unittest.TestCase):
    def test_inicializacion_valida_y_calculo(self):
        producto = Producto(" P001 ", " Teclado ", "Periféricos", 85000, 4)
        self.assertEqual(producto.codigo, "P001")
        self.assertEqual(producto.nombre, "Teclado")
        self.assertEqual(producto.calcular_valor(), 340000)

    def test_rechaza_datos_iniciales_invalidos(self):
        casos_invalidos = [
            ("   ", "Teclado", "Periféricos", 10, 1),
            ("P001", "  ", "Periféricos", 10, 1),
            ("P001", "Teclado", "No existe", 10, 1),
            ("P001", "Teclado", "Periféricos", 0, 1),
            ("P001", "Teclado", "Periféricos", -1, 1),
            ("P001", "Teclado", "Periféricos", 10, -1),
            ("P001", "Teclado", "Periféricos", float("inf"), 1),
        ]
        for datos in casos_invalidos:
            with self.subTest(datos=datos):
                with self.assertRaises(ValueError):
                    Producto(*datos)

    def test_cantidad_cero_y_codigo_solo_lectura(self):
        producto = Producto("P001", "Mouse", "Periféricos", 5, 0)
        self.assertEqual(producto.cantidad, 0)
        with self.assertRaises(AttributeError):
            producto.codigo = "P999"

    def test_actualizacion_de_cantidad(self):
        producto = Producto("P001", "Mouse", "Periféricos", 5, 2)
        self.assertTrue(producto.actualizar_existencias(10))
        self.assertEqual(producto.cantidad, 10)
        self.assertFalse(producto.actualizar_existencias(-3))
        self.assertEqual(producto.cantidad, 10)
        self.assertFalse(producto.actualizar_existencias(2.5))

    def test_conversion_de_precio_local(self):
        self.assertEqual(convertir_precio("85.000"), 85000.0)
        self.assertEqual(convertir_precio("1.234.567,89"), 1234567.89)
        self.assertEqual(convertir_precio("85000.50"), 85000.5)
        self.assertEqual(convertir_precio("85000"), 85000.0)


class PruebasInventario(unittest.TestCase):
    def setUp(self):
        self.inventario = Inventario()

    @staticmethod
    def crear(codigo, nombre, categoria, precio, cantidad):
        return Producto(codigo, nombre, categoria, precio, cantidad)

    def test_vacio(self):
        self.assertEqual(self.inventario.listar_productos(), [])
        self.assertEqual(self.inventario.productos_sin_stock(), [])
        self.assertEqual(
            self.inventario.resumen(),
            {
                "productos_registrados": 0,
                "unidades_disponibles": 0,
                "valor_total": 0,
                "categorias": set(),
            },
        )

    def test_registro_duplicado_busqueda_y_lista_copiada(self):
        p = self.crear("P001", "Teclado", "Periféricos", 85000, 4)
        self.assertTrue(self.inventario.registrar_producto(p))
        self.assertFalse(
            self.inventario.registrar_producto(
                self.crear("P001", "Otro", "Accesorios", 1, 1)
            )
        )
        self.assertIs(self.inventario.buscar_por_codigo("P001"), p)
        self.assertIsNone(self.inventario.buscar_por_codigo("P999"))
        copia = self.inventario.listar_productos()
        copia.clear()
        self.assertEqual(len(self.inventario.listar_productos()), 1)

    def test_sin_stock_y_actualizacion_solo_del_producto_objetivo(self):
        p1 = self.crear("P001", "Teclado", "Periféricos", 85000, 4)
        p2 = self.crear("P002", "Mouse", "Periféricos", 45000, 0)
        self.inventario.registrar_producto(p1)
        self.inventario.registrar_producto(p2)
        self.assertEqual([p.nombre for p in self.inventario.productos_sin_stock()], ["Mouse"])
        self.assertTrue(self.inventario.actualizar_existencias("P002", 5))
        self.assertEqual(p2.cantidad, 5)
        self.assertEqual(p1.cantidad, 4)
        self.assertFalse(self.inventario.actualizar_existencias("P002", -3))
        self.assertEqual(p2.cantidad, 5)
        self.assertFalse(self.inventario.actualizar_existencias("P999", 3))

    def test_eliminar_existente_e_inexistente(self):
        p = self.crear("P001", "Teclado", "Periféricos", 10, 1)
        self.inventario.registrar_producto(p)
        self.assertFalse(self.inventario.eliminar_producto("P999"))
        self.assertEqual(len(self.inventario.listar_productos()), 1)
        self.assertTrue(self.inventario.eliminar_producto("P001"))
        self.assertEqual(self.inventario.listar_productos(), [])

    def test_resumen_numerico_del_enunciado(self):
        productos = [
            self.crear("P001", "Teclado", "Periféricos", 85000, 4),
            self.crear("P002", "Mouse", "Periféricos", 45000, 0),
            self.crear("P003", "Disco SSD", "Componentes", 700000, 2),
        ]
        for producto in productos:
            self.assertTrue(self.inventario.registrar_producto(producto))
        resumen = self.inventario.resumen()
        self.assertEqual(resumen["productos_registrados"], 3)
        self.assertEqual(resumen["unidades_disponibles"], 6)
        self.assertEqual(resumen["valor_total"], 1740000.0)
        self.assertEqual(resumen["categorias"], {"Periféricos", "Componentes"})
        self.assertTrue(self.inventario.actualizar_existencias("P002", 5))
        resumen = self.inventario.resumen()
        self.assertEqual(resumen["unidades_disponibles"], 11)
        self.assertEqual(resumen["valor_total"], 1965000.0)

    def test_inventarios_independientes(self):
        primero = Inventario()
        segundo = Inventario()
        primero.registrar_producto(self.crear("P001", "Teclado", "Periféricos", 85000, 4))
        self.assertEqual(len(primero.listar_productos()), 1)
        self.assertEqual(len(segundo.listar_productos()), 0)

    def test_reto_de_ampliacion(self):
        self.inventario.registrar_producto(self.crear("P001", "Mouse", "Periféricos", 45, 1))
        self.inventario.registrar_producto(self.crear("P002", "Adaptador", "Accesorios", 10, 2))
        self.assertEqual(len(self.inventario.buscar_por_categoria("Periféricos")), 1)
        self.assertEqual(self.inventario.listar_ordenados_por_nombre()[0].nombre, "Adaptador")
        self.assertEqual(self.inventario.mapa_codigos_nombres(), {"P001": "Mouse", "P002": "Adaptador"})
        self.assertEqual(self.inventario.producto_mayor_valor().codigo, "P001")

    def test_categorias_son_las_del_enunciado(self):
        self.assertEqual(CATEGORIAS, ("Periféricos", "Componentes", "Accesorios"))


if __name__ == "__main__":
    unittest.main()
