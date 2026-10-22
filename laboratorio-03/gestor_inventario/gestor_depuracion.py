"""Reto de depuración (sección 20): seis errores provocados y corregidos.

Cada bloque reproduce el error en una clase de demostración (el proyecto real
NO se modifica) y muestra la corrección. Ejecutar: python gestor_depuracion.py
"""


# ---------------------------------------------------------------------------
# 1. Lista compartida a nivel de clase
# ---------------------------------------------------------------------------
class InventarioMalo:
    _productos = []  # ERROR: atributo de clase mutable, lo comparten todas las instancias.

    def registrar(self, producto):
        self._productos.append(producto)


a, b = InventarioMalo(), InventarioMalo()
a.registrar("Teclado")
print("1. Error  -> el segundo inventario ve:", b._productos)


class InventarioBueno:
    def __init__(self):
        self._productos = []  # CORRECCIÓN: cada objeto crea su propia lista.

    def registrar(self, producto):
        self._productos.append(producto)


a, b = InventarioBueno(), InventarioBueno()
a.registrar("Teclado")
print("1. Correcto -> el segundo inventario ve:", b._productos)
# Causa: una lista definida en el cuerpo de la clase es un único objeto compartido.


# ---------------------------------------------------------------------------
# 2. Propiedad que no existe
# ---------------------------------------------------------------------------
from producto import Producto  # noqa: E402

p = Producto("P001", "Teclado", "Periféricos", 85000, 4)
try:
    p.stock  # ERROR: la propiedad se llama "cantidad".
except AttributeError as error:
    print("2. Error  ->", error)
print("2. Correcto -> p.cantidad =", p.cantidad)
# Causa: nombre de atributo mal escrito; Python lo detecta al ejecutar, no antes.


# ---------------------------------------------------------------------------
# 3. Método de instancia sin self
# ---------------------------------------------------------------------------
class SinSelf:
    def mostrar():  # ERROR: falta el parámetro self.
        print("hola")


try:
    SinSelf().mostrar()
except TypeError as error:
    print("3. Error  ->", error)


class ConSelf:
    def mostrar(self):  # CORRECCIÓN
        print("3. Correcto -> hola")


ConSelf().mostrar()
# Causa: Python pasa el objeto como primer argumento al llamar al método.


# ---------------------------------------------------------------------------
# 4. Producto con cantidad negativa
# ---------------------------------------------------------------------------
class ProductoSinValidar:
    def __init__(self, cantidad):
        self._cantidad = cantidad  # ERROR: no se valida en el constructor.


print("4. Error  -> cantidad aceptada:", ProductoSinValidar(-10)._cantidad)
try:
    Producto("P002", "Mouse", "Periféricos", 45000, -10)
except ValueError as error:
    print("4. Correcto -> rechazado:", error)
# Causa: la validación solo existía al actualizar, no al crear el objeto.


# ---------------------------------------------------------------------------
# 5. Importación eliminada
# ---------------------------------------------------------------------------
codigo_sin_import = "inv = Inventario()"
try:
    exec(codigo_sin_import, {})  # ERROR: sin "from inventario import Inventario".
except NameError as error:
    print("5. Error  ->", error)
from inventario import Inventario  # noqa: E402  CORRECCIÓN

print("5. Correcto ->", type(Inventario()).__name__, "creado")
# Causa: un nombre usado sin importarlo no existe en el módulo.


# ---------------------------------------------------------------------------
# 6. Valor del inventario sumando precios sin multiplicar por cantidades
# ---------------------------------------------------------------------------
inv = Inventario()
inv.registrar_producto(Producto("P001", "Teclado", "Periféricos", 85000, 4))
inv.registrar_producto(Producto("P003", "Monitor", "Componentes", 700000, 2))
valor_mal = sum(x.precio for x in inv.listar_productos())  # ERROR
valor_bien = sum(x.calcular_valor() for x in inv.listar_productos())  # CORRECCIÓN
print("6. Error  ->", valor_mal, "| Correcto ->", valor_bien)
# Causa: faltaba precio * cantidad; calcular_valor() ya lo hace por producto.
