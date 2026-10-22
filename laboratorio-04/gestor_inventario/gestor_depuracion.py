"""Reto de depuración (sección 20): siete problemas reproducidos y corregidos.

Todo ocurre en un directorio temporal; el proyecto real no se modifica.
Ejecutar: python gestor_depuracion.py
"""

import csv
import json
import tempfile
from pathlib import Path

from almacenamiento import ErrorAlmacenamiento, cargar_inventario, guardar_inventario
from inventario import Inventario
from producto import Producto
from reportes import exportar_csv

tmp = Path(tempfile.mkdtemp())


def muestra():
    inv = Inventario()
    inv.registrar_producto(Producto("P001", "Teclado", "Periféricos", 85000, 4))
    inv.registrar_producto(Producto("P003", "Monitor", "Componentes", 700000, 2))
    return inv


# 1. Olvidar encoding="utf-8" -----------------------------------------------
ruta = tmp / "sin_encoding.json"
with ruta.open("w", encoding="utf-8") as f:                 # CORRECCIÓN
    json.dump([{"categoria": "Periféricos"}], f, ensure_ascii=False)
print("1. Con encoding utf-8 se lee:", json.loads(ruta.read_text(encoding="utf-8"))[0]["categoria"])
print("   (sin encoding, Windows usa cp1252 y 'Periféricos' puede leerse como 'PerifÃ©ricos')")
# Causa: el codec predeterminado depende del sistema operativo; hay que fijarlo siempre.

# 2. Ruta relativa que apunta a otra carpeta ----------------------------------
import os  # noqa: E402

import almacenamiento  # noqa: E402

os.chdir(tmp)  # se simula ejecutar el programa desde otra carpeta
print("2. Ruta relativa depende de dónde se ejecute:", Path("datos/productos.json").resolve())
print("   Ruta del proyecto (siempre la misma):     ", almacenamiento.RUTA_JSON)
# Causa: Path("datos/...") es relativa al directorio actual; BASE_DIR usa __file__.

# 3. json.dump directo de un Producto ----------------------------------------
try:
    json.dumps(Producto("P001", "Teclado", "Periféricos", 85000, 4))   # ERROR
except TypeError as error:
    print("3. Error ->", error)
print("   Correcto ->", json.dumps(Producto("P001", "Teclado", "Periféricos", 85000, 4).a_diccionario(), ensure_ascii=False))
# Causa: json solo conoce dict, list, str, números, bool y None; hay que usar a_diccionario().

# 4. Cargar JSON con código repetido sin validar -----------------------------
registro = {"codigo": "P1", "nombre": "A", "categoria": "Periféricos", "precio": 1, "cantidad": 1}
ruta = tmp / "duplicado.json"
ruta.write_text(json.dumps([registro, registro]), encoding="utf-8")
ingenuo = [Producto.desde_diccionario(d) for d in json.loads(ruta.read_text(encoding="utf-8"))]
print("4. Error -> carga sin validar unicidad:", len(ingenuo), "productos con el mismo código")
try:
    cargar_inventario(ruta)
except ErrorAlmacenamiento as error:
    print("   Correcto -> carga rechazada completa:", error)
# Causa: faltaba comprobar duplicados; Inventario.desde_datos usa un inventario temporal.

# 5. Sobrescribir un JSON dañado con [] --------------------------------------
ruta = tmp / "danado.json"
ruta.write_text('[{"codigo": "P001"', encoding="utf-8")
original = ruta.read_text(encoding="utf-8")
try:
    cargar_inventario(ruta)
except ErrorAlmacenamiento:
    pass                                    # CORRECCIÓN: se informa y NO se guarda []
print("5. Archivo dañado intacto tras el intento de carga:", ruta.read_text(encoding="utf-8") == original)
# Causa (versión errónea): except Exception: datos = []; guardar(datos) destruía datos recuperables.

# 6. CSV sumando precios en vez de precio * cantidad -------------------------
inv = muestra()
mal = sum(p.precio for p in inv.listar_productos())
ruta_csv = exportar_csv(inv, tmp / "inv.csv")
with ruta_csv.open(newline="", encoding="utf-8") as f:
    bien = sum(float(fila["valor_inventario"]) for fila in csv.DictReader(f))
print(f"6. Error -> {mal}   Correcto -> {bien}")
# Causa: faltaba multiplicar por cantidad; reportes.py usa producto.calcular_valor().

# 7. Modificar sin guardar y asumir que quedó persistido ---------------------
ruta = tmp / "persistencia.json"
inv = muestra()
guardar_inventario(inv, ruta)
inv.actualizar_existencias("P001", 99)               # cambio solo en memoria
print("7. Error -> en disco P001 sigue en", cargar_inventario(ruta).buscar_producto("P001").cantidad)
guardar_inventario(inv, ruta)                        # CORRECCIÓN: guardar y confirmar
print("   Correcto -> tras guardar queda en", cargar_inventario(ruta).buscar_producto("P001").cantidad)
# Causa: la memoria y el archivo son estados distintos; main.py guarda tras cada operación aceptada.
