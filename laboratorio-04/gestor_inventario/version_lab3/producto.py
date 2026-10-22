"""Representación y reglas individuales de un producto de inventario."""

import math

CATEGORIAS = ("Periféricos", "Componentes", "Accesorios")


class Producto:
    def __init__(self, codigo, nombre, categoria, precio, cantidad):
        if not isinstance(codigo, str) or not codigo.strip():
            raise ValueError("El código no puede estar vacío.")
        if not isinstance(nombre, str) or not nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        if not isinstance(categoria, str) or not categoria.strip():
            raise ValueError("La categoría no puede estar vacía.")

        codigo = codigo.strip()
        nombre = nombre.strip()
        categoria = categoria.strip()
        if categoria not in CATEGORIAS:
            raise ValueError(
                "La categoría no está autorizada. Usa: " + ", ".join(CATEGORIAS) + "."
            )
        if (
            isinstance(precio, bool)
            or not isinstance(precio, (int, float))
            or not math.isfinite(precio)
            or precio <= 0
        ):
            raise ValueError("El precio debe ser un número finito mayor que cero.")
        if isinstance(cantidad, bool) or not isinstance(cantidad, int) or cantidad < 0:
            raise ValueError("La cantidad debe ser un entero no negativo.")

        # Todos los valores se validan antes de guardar estado en el objeto.
        self._codigo = codigo
        self._nombre = nombre
        self._categoria = categoria
        self._precio = float(precio)
        self._cantidad = cantidad

    @property
    def codigo(self):
        """Identificador de solo consulta; no se ofrece un setter."""
        return self._codigo

    @property
    def nombre(self):
        return self._nombre

    @property
    def categoria(self):
        return self._categoria

    @property
    def precio(self):
        return self._precio

    @property
    def cantidad(self):
        return self._cantidad

    def actualizar_existencias(self, nueva_cantidad):
        """Actualiza cantidades enteras no negativas; devuelve False si no valen."""
        if (
            isinstance(nueva_cantidad, bool)
            or not isinstance(nueva_cantidad, int)
            or nueva_cantidad < 0
        ):
            return False
        self._cantidad = nueva_cantidad
        return True

    def calcular_valor(self):
        """Devuelve el valor total de las existencias de este producto."""
        return self._precio * self._cantidad

    def __str__(self):
        return (
            f"{self.codigo} - {self.nombre} - {self.categoria} - "
            f"${self.precio} - {self.cantidad} unidades"
        )
