# Laboratorio 02 — Decisiones, ciclos y colecciones en Python

Ejercicios del segundo laboratorio de Python (ADSO): decisiones con `if/elif/else`, condiciones
compuestas, ciclos `for` y `while`, listas, tuplas, conjuntos, diccionarios, comprensiones y la
actividad integradora **Gestor de inventario** (en memoria, sin archivos ni bases de datos).

## Requisitos

- Python 3 (`python --version`, o `py` / `python3` según el equipo).

## Cómo ejecutar

Desde la carpeta `laboratorio-02`:

```bash
python nombre_del_archivo.py
```

## Contenido

| Práctica | Tema | Archivos principales |
|---|---|---|
| 2.1 | Comparaciones y decisiones | `comparaciones.py`, `disponibilidad.py`, `validar_edad.py`, `clasificar_numero.py`, `clasificar_nota.py`, `comparar_texto.py`, `error_indentacion*.py`, `costo_envio.py` |
| 2.2 | Condiciones compuestas | `acceso_actividad.py`, `operador_or.py`, `operador_not.py`, `predice.py`, `acceso_sala.py`, `rango_edad.py`, `validar_compra.py`, `depuracion*.py`, `evaluar_solicitud.py` |
| 2.3 | Ciclos | `contador_for.py`, `tabla_multiplicar.py`, `sumar_numeros.py`, `promedio_notas.py`, `contador_while.py`, `hasta_cero.py`, `suma_interactiva.py`, `menu_repetitivo.py`, `ciclo_queno_termina*.py`, `control_ahorros.py` |
| 2.4 | Listas | `primera_lista.py`, `ciudades.py`, `append.py`, `invitados.py`, `recorrer.py`, `lista_materias.py`, `sin_duplicados.py`, `operaciones_lista.py`, `cambios_inventario.py`, `copias_listas.py`, `calificaciones_lista.py`, `indice_inexistente.py`, `lista_tareas.py` |
| 2.5 | Tuplas | `primeras_tuplas.py`, `mutabilidad.py`, `tupla_un_elemento.py`, `desempaquetar_tupla.py`, `ubicaciones.py`, `categorias.py`, `categorias_tupla.py`, `desempaquetado_incorreccto*.py` |
| 2.6 | Conjuntos | `primer_conjunto.py`, `conjunto_vacio.py`, `ciudades_unicas.py`, `etiquetas.py`, `agregar_eliminar.py`, `participantes.py`, `operaciones_conjuntos.py`, `inscripciones_talleres.py` |
| 2.7 | Diccionarios | `primer_diccionario.py`, `perfil_diccionario.py`, `recorrer_diccionario.py`, `actualizar_*.py`, `lista_diccionarios.py`, `valor_inventario.py`, `catalogo_diccionarios.py`, `estructuras_anidadas.py`, `buscar_producto.py`, `catalogo_libros.py` |
| 2.8 | Comprensiones | `cuadrados.py`, `precios_con_impuesto.py`, `filtrar_numeros.py`, `notas_aprobadas.py`, `normalizar_codigos.py`, `informes_inventario.py`, `informe_comprensiones.py`, ... |
| 2.9 | Reto integrador | `gestor_inventario.py`, `pruebas_gestor.py`, `gestor_inventario_ampliado.py`, `gestor_depuracion.py` |

## Gestor de inventario (`gestor_inventario.py`)

Menú que se repite hasta elegir `0`:

```text
1. Registrar producto          5. Eliminar producto
2. Listar productos            6. Consultar productos sin stock
3. Buscar por código           7. Resumen del inventario
4. Actualizar existencias      0. Salir
```

- Cada producto es un **diccionario** (`codigo`, `nombre`, `categoria`, `precio`, `cantidad`) y todos están en una **lista**.
- Las categorías permitidas están en una **tupla** (`CATEGORIAS`).
- Los informes usan **comprensiones**: de lista (sin stock) y de conjunto (categorías utilizadas).
- Validaciones: código repetido, campos vacíos, categoría no permitida, precio no positivo y cantidad negativa.

```bash
python gestor_inventario.py
```

> Escribe los precios sin puntos de miles (`85000`, no `85.000`).

## Pruebas

```bash
python pruebas_gestor.py
```

Ejecuta las pruebas obligatorias del laboratorio (listar vacío, duplicados, validaciones, búsqueda,
actualización, eliminación, resumen y la comprobación numérica: 3 productos, 6 unidades,
$1740000.0 y 2 categorías). Resultado actual: **19/19 pruebas correctas**.

## Informe

[`informe/Informe_Laboratorio_02.pdf`](informe/Informe_Laboratorio_02.pdf)
