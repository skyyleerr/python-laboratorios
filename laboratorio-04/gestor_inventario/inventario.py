"""Gestor de dominio: administra objetos Producto y no realiza input()."""
from producto import Producto

class Inventario:
    def __init__(self, productos=None):
        self._productos = []
        if productos is not None:
            for producto in productos:
                if not self.registrar_producto(producto):
                    raise ValueError(f"Código duplicado: {producto.codigo}")

    def registrar_producto(self, producto):
        if not isinstance(producto, Producto):
            raise TypeError("Solo se pueden registrar objetos Producto.")
        if self.buscar_producto(producto.codigo) is not None:
            return False
        self._productos.append(producto)
        return True

    def buscar_producto(self, codigo):
        codigo = str(codigo).strip().upper()
        return next((p for p in self._productos if p.codigo == codigo), None)

    def listar_productos(self): return self._productos.copy()

    def actualizar_existencias(self, codigo, cantidad):
        producto = self.buscar_producto(codigo)
        return producto is not None and producto.actualizar_existencias(cantidad)

    def eliminar_producto(self, codigo):
        producto = self.buscar_producto(codigo)
        if producto is None: return False
        self._productos.remove(producto)
        return True

    def productos_sin_stock(self):
        return [p for p in self._productos if p.cantidad == 0]

    def resumen(self):
        return {
            "productos_registrados": len(self._productos),
            "unidades_disponibles": sum(p.cantidad for p in self._productos),
            "valor_total": sum(p.calcular_valor() for p in self._productos),
            "categorias": {p.categoria for p in self._productos},
        }

    def exportar_datos(self): return [p.a_diccionario() for p in self._productos]

    @classmethod
    def desde_datos(cls, datos):
        if not isinstance(datos, list):
            raise ValueError("El JSON debe contener una lista de productos.")
        # Construir en un inventario temporal: un error no produce carga parcial.
        temporal = cls()
        for registro in datos:
            producto = Producto.desde_diccionario(registro)
            if not temporal.registrar_producto(producto):
                raise ValueError(f"Código duplicado en archivo: {producto.codigo}")
        return temporal
