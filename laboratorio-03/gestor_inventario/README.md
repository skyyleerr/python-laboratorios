# Gestor de inventario orientado a objetos (Laboratorio 3)

Aplicación de consola que registra, lista, busca, actualiza y elimina productos y genera informes.
Es la transformación del gestor procedural del Laboratorio 2 (`laboratorio-02/gestor_inventario.py`,
lista de diccionarios y un solo archivo) en una aplicación con **clases y módulos**.

## Estructura

```text
gestor_inventario/
├── main.py                    # menú, input(), mensajes
├── producto.py                # clase Producto
├── inventario.py              # clase Inventario
├── pruebas_independencia.py   # dos Inventario con colecciones separadas
├── pruebas_obligatorias.py    # 18 pruebas del menú y de las reglas (sección 16-18)
├── test_gestor.py             # 13 pruebas unitarias de las clases
├── gestor_depuracion.py       # seis errores provocados y corregidos
└── README.md
```

## Ejecución

Desde la carpeta `gestor_inventario`:

```bash
python main.py                          # aplicación (py main.py o python3 main.py según el equipo)
python pruebas_independencia.py         # Primero: 1 / Segundo: 0
python -m unittest -v                   # 13 pruebas unitarias
python pruebas_obligatorias.py          # 18 pruebas del enunciado
python gestor_depuracion.py             # reto de depuración
```

No se necesitan paquetes externos (solo Python 3.8 o superior).

## Responsabilidad de cada módulo

| Archivo | Responsabilidad |
|---|---|
| `producto.py` | `Producto`: guarda los datos, **valida desde `__init__`** (código y nombre no vacíos, categoría autorizada, precio > 0, cantidad ≥ 0), expone propiedades de solo lectura, actualiza existencias y calcula `precio * cantidad`. Declara `CATEGORIAS` una sola vez. |
| `inventario.py` | `Inventario`: guarda su propia lista `self._productos`; registra (sin duplicados), lista (copia), busca, actualiza, elimina, filtra sin stock y arma el resumen. **No usa `input()` ni `print()`.** |
| `main.py` | Interacción: menú, lectura de datos con reintento, captura de `ValueError` y mensajes al usuario. |

### Clase `Producto`

- Atributos internos: `_codigo`, `_nombre`, `_categoria`, `_precio`, `_cantidad`.
- Propiedades: `codigo`, `nombre`, `categoria`, `precio`, `cantidad` (sin setter: el código no puede cambiarse).
- Métodos: `actualizar_existencias(nueva_cantidad) -> bool`, `calcular_valor() -> float`, `__str__()`.

### Clase `Inventario`

`registrar_producto`, `listar_productos`, `buscar_por_codigo`, `actualizar_existencias`,
`eliminar_producto`, `productos_sin_stock` (comprensión de lista) y `resumen` (comprensión de conjunto para
las categorías). Extras del reto de ampliación: `buscar_por_categoria`, `listar_ordenados_por_nombre`,
`producto_mayor_valor`, `mapa_codigos_nombres`.

## Pruebas realizadas

| Caso | Resultado |
|---|---|
| Inventario vacío | Mensaje "El inventario está vacío." y resumen en cero |
| Registrar P001 / repetirlo | Aceptado / rechazado |
| Código o nombre vacío | Se vuelve a pedir el dato; no se guarda nada parcial |
| Categoría no permitida | Rechazada con mensaje claro |
| Precio 0 o negativo | Se vuelve a pedir |
| Cantidad negativa / cero | Se vuelve a pedir / producto válido sin stock |
| Buscar P001 / P999 | Muestra el producto / "Producto no registrado." |
| Actualizar a 10 / a -3 | Solo cambia la cantidad / se rechaza y conserva el dato |
| Eliminar existente / inexistente | Elimina / informa sin fallar |
| Texto en campo numérico | Mensaje y nueva oportunidad |
| Comprobación numérica (P001, P002, P003) | 3 productos, 6 unidades, $1740000.0, 2 categorías |
| Tras actualizar P002 a 5 | 11 unidades, $1965000.0 |
| Dos inventarios | Primero: 1, Segundo: 0 |

Resultado: 13 pruebas unitarias + 18 pruebas del enunciado, todas aprobadas.

> Nota: escribe los precios sin separadores (`85000`). `main.py` también interpreta `85.000` como 85000,
> según la costumbre colombiana.
