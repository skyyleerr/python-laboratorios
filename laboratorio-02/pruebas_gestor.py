"""Pruebas automáticas del gestor de inventario (Práctica 2.9).

Ejecuta gestor_inventario.py enviando las opciones del menú por la entrada
estándar y comprueba el comportamiento esperado de cada prueba obligatoria.

Uso:  python pruebas_gestor.py
"""
import os
import subprocess
import sys

PROGRAMA = os.path.join(os.path.dirname(os.path.abspath(__file__)), "gestor_inventario.py")


def ejecutar(*lineas):
    """Envía las líneas al programa (siempre termina con la opción 0) y devuelve la salida."""
    entrada = "\n".join(list(lineas) + ["0"]) + "\n"
    r = subprocess.run([sys.executable, PROGRAMA], input=entrada,
                       capture_output=True, text=True, encoding="utf-8", timeout=20)
    return r.stdout, r.returncode


def registrar(cod, nom, cat, precio, cant):
    return ["1", cod, nom, cat, str(precio), str(cant)]


P1 = registrar("P001", "Teclado", "Periféricos", 85000, 4)
P2 = registrar("P002", "Mouse", "Periféricos", 45000, 0)
P3 = registrar("P003", "Disco SSD", "Componentes", 700000, 2)

# (nombre de la prueba, líneas de entrada, textos que DEBEN aparecer, textos que NO deben aparecer)
PRUEBAS = [
    ("Listar sin productos", ["2"], ["No hay productos registrados."], []),
    ("Registrar P001", P1, ["Producto registrado."], []),
    ("Registrar P001 nuevamente", P1 + P1, ["ya existe un producto con ese código"], []),
    ("Nombre vacío", ["1", "P001", "", "Periféricos"], ["no pueden estar vacíos"], ["Producto registrado."]),
    ("Nombre solo espacios", ["1", "P001", "   ", "Periféricos"], ["no pueden estar vacíos"], ["Producto registrado."]),
    ("Categoría fuera de la tupla", ["1", "P001", "Teclado", "Ropa"], ["categoría no válida"], ["Producto registrado."]),
    ("Precio negativo", registrar("P001", "Teclado", "Periféricos", -5, 1), ["precio debe ser mayor que cero"], ["Producto registrado."]),
    ("Cantidad negativa", registrar("P001", "Teclado", "Periféricos", 5, -1), ["cantidad no puede ser negativa"], ["Producto registrado."]),
    ("Cantidad cero aceptada", P2 + ["6"], ["Producto registrado.", "- Mouse"], []),
    ("Buscar P001", P1 + ["3", "P001"], ["Teclado", "Periféricos"], []),
    ("Buscar código desconocido", ["3", "P999"], ["no existe"], []),
    ("Actualizar a 10 unidades", P1 + ["4", "P001", "10", "3", "P001"], ["Existencias actualizadas.", "Cantidad: 10", "Teclado"], []),
    ("Actualizar a -3 conserva cantidad", P1 + ["4", "P001", "-3", "3", "P001"], ["Se conserva la cantidad anterior.", "Cantidad: 4"], []),
    ("Eliminar existente", P1 + ["5", "P001", "2"], ["Producto eliminado.", "No hay productos registrados."], []),
    ("Eliminar inexistente no falla", ["5", "P999"], ["no existe"], ["Traceback"]),
    ("Resumen enunciado (P001, P002)", P1 + P2 + ["2", "6", "7"],
     ["P001 - Teclado - Periféricos - $85000.0 - 4 unidades", "P002 - Mouse - Periféricos - $45000.0 - 0 unidades",
      "- Mouse", "Productos: 2", "Unidades: 4", "Valor del inventario: $340000.0", "Categorías utilizadas: Periféricos"], []),
    ("Comprobación numérica (P001-P003)", P1 + P2 + P3 + ["6", "7"],
     ["Productos: 3", "Unidades: 6", "Valor del inventario: $1740000.0",
      "Categorías utilizadas: Componentes, Periféricos", "- Mouse"], []),
    ("Opción no válida", ["9"], ["Opción no válida."], ["Traceback"]),
    ("Salir", [], ["Programa finalizado."], []),
]

if __name__ == "__main__":
    fallos = 0
    for nombre, entrada, deben, no_deben in PRUEBAS:
        salida, codigo = ejecutar(*entrada)
        problemas = [f"falta: {t!r}" for t in deben if t not in salida]
        problemas += [f"sobra: {t!r}" for t in no_deben if t in salida]
        if codigo != 0:
            problemas.append(f"el programa terminó con error (código {codigo})")
        fallos += bool(problemas)
        print(f"[{'OK ' if not problemas else 'FALLA'}] {nombre}")
        for p in problemas:
            print("        " + p)
    print(f"\n{len(PRUEBAS) - fallos}/{len(PRUEBAS)} pruebas correctas")
    sys.exit(1 if fallos else 0)
