# Python — Laboratorios

Repositorio personal de **Anthony Córdova Calderón** (ficha 3388087). Cada laboratorio vive en su carpeta y se
conserva completo para mostrar la evolución técnica.

| Lab | Carpeta | Tema | Proyecto integrador |
|---|---|---|---|
| 01 | [`laboratorio-01/`](laboratorio-01/) | Fundamentos: variables, entrada/salida, cálculos | Cotizador |
| 02 | [`laboratorio-02/`](laboratorio-02/) | Decisiones, ciclos y colecciones | Gestor de inventario procedural (listas y diccionarios) |
| 03 | [`laboratorio-03/`](laboratorio-03/) | Funciones, módulos y POO | Gestor orientado a objetos (`Producto` + `Inventario`) |
| 04 | [`laboratorio-04/`](laboratorio-04/) | Excepciones, archivos, JSON/CSV | Gestor persistente (almacenamiento + reportes) |

## Cómo ejecutar cada etapa

```bash
cd laboratorio-01                              # ver el README de la carpeta
cd laboratorio-02 && python gestor_inventario.py                  # procedural
cd laboratorio-03/gestor_inventario && python main.py             # orientado a objetos
cd laboratorio-04/gestor_inventario && python main.py             # persistente (JSON + CSV)
cd laboratorio-04/gestor_inventario && python -m unittest -v      # pruebas del lab 4
```

## Evolución del proyecto

1. **Lab 1:** programas lineales que piden datos y calculan (cotizador).
2. **Lab 2:** el inventario aparece como una lista de diccionarios con menú, validaciones y comprensiones, todo en un archivo; los datos se pierden al cerrar.
3. **Lab 3:** el mismo inventario se reorganiza en `Producto`, `Inventario` y `main.py`; las reglas pasan a las clases y la interacción queda aparte.
4. **Lab 4:** se agregan `almacenamiento.py` (JSON) y `reportes.py` (CSV); los productos se recuperan entre ejecuciones, un archivo dañado nunca se sobrescribe y cada módulo tiene una responsabilidad única.
