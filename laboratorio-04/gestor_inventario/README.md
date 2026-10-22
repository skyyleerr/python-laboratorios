# Gestor de inventario persistente (Laboratorio 4)

Evolución del gestor orientado a objetos del Laboratorio 3 (`version_lab3/` conserva esa versión para
compararla). Ahora el inventario **se conserva entre ejecuciones** en un archivo JSON y puede exportarse a CSV.

## Estructura

```text
gestor_inventario/
├── main.py                  # menú, input(), mensajes y coordinación
├── producto.py              # Producto: validaciones, a_diccionario(), desde_diccionario()
├── inventario.py            # Inventario: colección, exportar_datos(), desde_datos()
├── almacenamiento.py        # lectura/escritura del JSON (único módulo que conoce datos/productos.json)
├── reportes.py              # exportación CSV (único módulo que conoce reportes/inventario.csv)
├── test_gestor.py           # 10 pruebas unitarias
├── pruebas_obligatorias.py  # 16 pruebas de sesiones completas (reinicio, JSON dañado, CSV, etc.)
├── gestor_depuracion.py     # siete problemas del reto de depuración, reproducidos y corregidos
├── version_lab3/            # copia del gestor del Laboratorio 3 (sin cambios)
├── datos/productos.json     # se genera al guardar (no se versiona)
└── reportes/inventario.csv  # se genera al exportar (no se versiona)
```

## Ejecución

Desde cualquier carpeta (las rutas se calculan con `Path(__file__)`):

```bash
python main.py                      # py main.py o python3 main.py según el equipo
python -m unittest -v               # 10 pruebas unitarias
python pruebas_obligatorias.py      # 16 pruebas de sesión
python gestor_depuracion.py         # reto de depuración
```

Sin paquetes externos: solo `pathlib`, `json`, `csv`, `tempfile`, `math`.

## Responsabilidades

| Módulo | Responsabilidad | ¿Conoce el sistema de archivos? |
|---|---|---|
| `producto.py` | Reglas de un producto y conversión a/desde diccionario | No |
| `inventario.py` | Colección de productos; `exportar_datos()` y `desde_datos()` (carga en inventario temporal) | No |
| `almacenamiento.py` | `guardar_inventario()` (escritura atómica con archivo temporal) y `cargar_inventario()` | Sí (JSON) |
| `reportes.py` | `exportar_csv()` con `valor_inventario = precio * cantidad` | Sí (CSV) |
| `main.py` | Menú, lectura con reintento, captura de excepciones y mensajes | No directamente |

Ninguno de los módulos, salvo `main.py`, usa `input()`.

## Comportamiento ante archivos

| Situación | Resultado |
|---|---|
| `productos.json` no existe | Inventario vacío, sin error |
| Existe y es válido | Se recuperan todos los productos (se reconstruyen con las validaciones del constructor) |
| JSON con error de sintaxis, estructura inesperada, registro inválido o código repetido | Se informa, **no se carga nada parcial** y la aplicación entra en modo solo consulta: registrar, actualizar, eliminar y guardar quedan bloqueados, así el archivo no se sobrescribe |
| Falla la escritura | Se informa que el cambio queda solo en memoria; no se anuncia «guardado» |

El guardado escribe primero en un archivo temporal y lo reemplaza al terminar, por lo que un fallo a mitad de
escritura no deja el JSON original incompleto.

## Pruebas realizadas

Resultados: **10 pruebas unitarias + 16 pruebas de sesión, todas aprobadas.**

| Situación | Resultado |
|---|---|
| Primera ejecución sin JSON | Inventario vacío |
| Guardar 2 productos, cerrar y reiniciar | Se recuperan los 2 |
| Código duplicado / categoría desconocida / precio negativo, `nan`, `inf` / cantidad negativa | Rechazados; el JSON no cambia |
| Cantidad cero | Se acepta (producto sin stock) |
| Actualizar y eliminar, luego reiniciar | Los cambios persisten |
| Texto no numérico | Mensaje y nueva oportunidad |
| JSON sin una coma | Se informa, archivo intacto, operaciones bloqueadas; al restaurar la copia se recuperan los 3 productos |
| JSON con estructura inesperada o código repetido | Carga rechazada completa, archivo intacto |
| Error de escritura simulado | Mensaje «queda solo en memoria», sin «Guardado en:» |
| CSV | Encabezados correctos y `valor_inventario` = 340000.0 / 225000.0 / 1400000.0 |
| Prueba numérica (P001, P002, P003) | 3 productos, 6 unidades, $1740000.0; con P002 = 5: 11 unidades, $1965000.0 |
