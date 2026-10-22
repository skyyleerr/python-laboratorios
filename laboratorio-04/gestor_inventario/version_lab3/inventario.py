"""Administración de una colección independiente de objetos Producto."""

from producto import Producto


class Inventario:
    def __init__(self):
        # Atributo de instancia: inventarios distintos nunca comparten la lista.
        self._productos = []

    def registrar_producto(self, producto):
        """Agrega el producto si es válido y su código no está registrado."""
        if not isinstance(producto, Producto):
            return False
        if self.buscar_por_codigo(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def listar_productos(self):
        """Devuelve una copia superficial para proteger la lista interna."""
        return self._productos.copy()

    def buscar_por_codigo(self, codigo):
        if not isinstance(codigo, str):
            return None
        codigo = codigo.strip()
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def actualizar_existencias(self, codigo, nueva_cantidad):
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        return producto.actualizar_existencias(nueva_cantidad)

    def eliminar_producto(self, codigo):
        producto = self.buscar_por_codigo(codigo)
        if producto is None:
            return False
        self._productos.remove(producto)
        return True

    def productos_sin_stock(self):
        """Devuelve objetos Producto agotados usando comprensión de lista."""
        return [producto for producto in self._productos if producto.cantidad == 0]

    def resumen(self):
        """Devuelve productos, unidades, valor y categorías como set."""
        return {
            "productos_registrados": len(self._productos),
            "unidades_disponibles": sum(
                producto.cantidad for producto in self._productos
            ),
            "valor_total": sum(
                producto.calcular_valor() for producto in self._productos
            ),
            "categorias": {producto.categoria for producto in self._productos},
        }

    # Funciones opcionales del reto de ampliación.
    def buscar_por_categoria(self, categoria):
        return [p for p in self._productos if p.categoria == categoria]

    def listar_ordenados_por_nombre(self):
        return sorted(self._productos, key=lambda producto: producto.nombre.casefold())

    def producto_mayor_valor(self):
        return max(self._productos, key=lambda p: p.calcular_valor(), default=None)

    def mapa_codigos_nombres(self):
        return {producto.codigo: producto.nombre for producto in self._productos}
