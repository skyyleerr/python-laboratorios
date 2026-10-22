"""Pruebas automáticas del cotizador (Práctica 1.5).

Ejecuta cotizador_compra.py enviando datos por la entrada estándar y compara
el resumen con los resultados esperados del laboratorio.

Uso:  python pruebas_cotizador.py
"""
import os
import subprocess
import sys

CARPETA = os.path.dirname(os.path.abspath(__file__))
PROGRAMA = os.path.join(CARPETA, "cotizador_compra.py")


def ejecutar(cliente, producto, precio, cantidad, descuento, impuesto):
    entrada = "\n".join([cliente, producto, precio, cantidad, descuento, impuesto]) + "\n"
    r = subprocess.run([sys.executable, PROGRAMA], input=entrada,
                       capture_output=True, text=True, encoding="utf-8")
    return r.stdout


# (descripción, datos de entrada, líneas que deben aparecer en el resumen)
CASOS = [
    ("Ejemplo del enunciado",
     ("Laura", "Teclado mecánico", "180000", "2", "10", "19"),
     ["Cliente: Laura", "Producto: Teclado mecánico", "Precio unitario: $180000.0",
      "Cantidad: 2", "Subtotal: $360000.0", "Descuento: $36000.0",
      "Base: $324000.0", "Impuesto: $61560.0", "TOTAL: $385560.0"]),
    ("Caso 1", ("Ana", "Mouse", "100000", "2", "10", "0"), ["TOTAL: $180000.0"]),
    ("Caso 2", ("Ana", "Mouse", "50000", "3", "0", "0"), ["TOTAL: $150000.0"]),
    ("Caso 3", ("Ana", "Mouse", "80000", "5", "25", "0"), ["TOTAL: $300000.0"]),
    # Cálculo manual: 100000 + 19 % = 119000.0
    ("Caso 4", ("Ana", "Mouse", "100000", "1", "0", "19"), ["TOTAL: $119000.0"]),
]

if __name__ == "__main__":
    fallos = 0
    for nombre, datos, esperadas in CASOS:
        salida = ejecutar(*datos)
        faltan = [l for l in esperadas if l not in salida.splitlines()]
        estado = "OK " if not faltan else "FALLA"
        fallos += bool(faltan)
        print(f"[{estado}] {nombre}")
        for l in faltan:
            print(f"        esperado: {l!r}")
    print(f"\n{len(CASOS) - fallos}/{len(CASOS)} casos correctos")
    sys.exit(1 if fallos else 0)
