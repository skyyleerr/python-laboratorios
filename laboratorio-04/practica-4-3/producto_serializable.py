import json
class Producto:
    def __init__(self, codigo, nombre):
        self.codigo, self.nombre = codigo, nombre
    def a_diccionario(self):
        return {"codigo": self.codigo, "nombre": self.nombre}
    @classmethod
    def desde_diccionario(cls, datos):
        return cls(datos["codigo"], datos["nombre"])

producto = Producto("P001", "Teclado")
texto = json.dumps(producto.a_diccionario(), ensure_ascii=False)
restaurado = Producto.desde_diccionario(json.loads(texto))
print(texto)
print(type(restaurado).__name__, restaurado.codigo, restaurado.nombre)
