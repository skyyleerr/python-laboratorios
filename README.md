# Python — Laboratorios

<<<<<<< HEAD
Repositorio personal de **Anthony Córdova Calderón** (ficha 3388087). Cada laboratorio vive en su carpeta
y se conserva completo para mostrar la evolución técnica.

| Laboratorio | Carpeta | Tema | Proyecto integrador |
|---|---|---|---|
| 01 | [`laboratorio-01/`](laboratorio-01/) | Fundamentos: variables, entrada/salida y cálculos | Cotizador |
| 02 | [`laboratorio-02/`](laboratorio-02/) | Decisiones, ciclos y colecciones | Gestor de inventario procedural (listas y diccionarios) |
| 03 | [`laboratorio-03/`](laboratorio-03/) | Funciones, módulos y POO | Gestor de inventario orientado a objetos (`Producto` + `Inventario`) |
=======
Repositorio personal de **Anthony Córdova Calderón** (ficha 3388087, ADSO) para los cuatro laboratorios de Python.

| Laboratorio | Tema | Carpeta |
|---|---|---|
| 01 | Primeros pasos: variables, tipos, operadores, `input()` y cotizador | [`laboratorio-01/`](laboratorio-01/) |
| 02 | Decisiones, ciclos y colecciones; gestor de inventario | [`laboratorio-02/`](laboratorio-02/) |
| 03 | _pendiente_ | — |
| 04 | _pendiente_ | — |
>>>>>>> d103dd188e8eefb79a90cb60e7d50d5ec48b5169

## Cómo ejecutar

```bash
<<<<<<< HEAD
cd laboratorio-02 && python gestor_inventario.py                 # versión procedural
cd laboratorio-03/gestor_inventario && python main.py            # versión orientada a objetos
cd laboratorio-03/gestor_inventario && python -m unittest -v     # pruebas
```

## Evolución del gestor de inventario

- **Lab 2:** un archivo, productos como diccionarios dentro de una lista, todo el código en un ciclo `while`.
- **Lab 3:** tres módulos; `Producto` valida y protege sus datos, `Inventario` administra la colección y
  `main.py` se limita a la interacción con el usuario.
=======
cd laboratorio-01 && python cotizador_compra.py     # Laboratorio 01
cd laboratorio-02 && python gestor_inventario.py    # Laboratorio 02
```

Pruebas automáticas: `python pruebas_cotizador.py` (lab. 01) y `python pruebas_gestor.py` (lab. 02).
>>>>>>> d103dd188e8eefb79a90cb60e7d50d5ec48b5169
