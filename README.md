# Python — Laboratorios

Repositorio personal de **Anthony Córdova Calderón** (ficha 3388087). Cada laboratorio vive en su carpeta
y se conserva completo para mostrar la evolución técnica.

| Laboratorio | Carpeta | Tema | Proyecto integrador |
|---|---|---|---|
| 01 | [`laboratorio-01/`](laboratorio-01/) | Fundamentos: variables, entrada/salida y cálculos | Cotizador |
| 02 | [`laboratorio-02/`](laboratorio-02/) | Decisiones, ciclos y colecciones | Gestor de inventario procedural (listas y diccionarios) |
| 03 | [`laboratorio-03/`](laboratorio-03/) | Funciones, módulos y POO | Gestor de inventario orientado a objetos (`Producto` + `Inventario`) |

## Cómo ejecutar

```bash
cd laboratorio-02 && python gestor_inventario.py                 # versión procedural
cd laboratorio-03/gestor_inventario && python main.py            # versión orientada a objetos
cd laboratorio-03/gestor_inventario && python -m unittest -v     # pruebas
```

## Evolución del gestor de inventario

- **Lab 2:** un archivo, productos como diccionarios dentro de una lista, todo el código en un ciclo `while`.
- **Lab 3:** tres módulos; `Producto` valida y protege sus datos, `Inventario` administra la colección y
  `main.py` se limita a la interacción con el usuario.
