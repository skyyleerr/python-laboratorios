"""Modelo validado de producto; no realiza entrada/salida interactiva."""
import math

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")

class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código es obligatorio.")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre es obligatorio.")
        if not isinstance(categoria, str) or categoria not in CATEGORIAS:
            raise ValueError(f"Categoría no permitida. Usa: {', '.join(CATEGORIAS)}")
        if isinstance(precio, bool) or not isinstance(precio, (int, float)):
            raise TypeError("El precio debe ser numérico.")
        if not math.isfinite(precio) or precio <= 0:
            raise ValueError("El precio debe ser finito y positivo.")
        if isinstance(cantidad, bool) or not isinstance(cantidad, int):
            raise TypeError("La cantidad debe ser entera.")
        if cantidad < 0:
            raise ValueError("La cantidad no puede ser negativa.")
        self._codigo = codigo.strip().upper()
        self._nombre = nombre.strip()
        self._categoria = categoria
        self._precio = float(precio)
        self._cantidad = cantidad

    @property
    def codigo(self): return self._codigo
    @property
    def nombre(self): return self._nombre
    @property
    def categoria(self): return self._categoria
    @property
    def precio(self): return self._precio
    @property
    def cantidad(self): return self._cantidad

    def actualizar_existencias(self, cantidad):
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad < 0:
            return False
        self._cantidad = cantidad
        return True

    def calcular_valor(self): return self._precio * self._cantidad

    def a_diccionario(self):
        return {"codigo": self.codigo, "nombre": self.nombre,
                "categoria": self.categoria, "precio": self.precio,
                "cantidad": self.cantidad}

    @classmethod
    def desde_diccionario(cls, datos):
        if not isinstance(datos, dict):
            raise ValueError("Cada producto debe ser un objeto JSON.")
        campos = ("codigo", "nombre", "categoria", "precio", "cantidad")
        faltantes = [campo for campo in campos if campo not in datos]
        if faltantes:
            raise ValueError("Faltan campos: " + ", ".join(faltantes))
        return cls(*(datos[campo] for campo in campos))

    def __repr__(self):
        return (f"Producto({self.codigo!r}, {self.nombre!r}, {self.categoria!r}, "
                f"{self.precio!r}, {self.cantidad!r})")
