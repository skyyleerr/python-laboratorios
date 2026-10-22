# Laboratorio 01 — Primeros pasos con Python

Ejercicios del primer laboratorio de Python (ADSO): entorno de trabajo, ejecución de
archivos `.py`, variables, tipos de datos, operadores, entrada con `input()` y la
actividad integradora **Cotizador de compra**.

## Requisitos

- Python 3 (`python --version`, o `py` / `python3` según el equipo).
- Visual Studio Code con la extensión *Python* (opcional; también se ejecuta desde la terminal).

## Cómo ejecutar

Desde la carpeta `laboratorio-01`:

```bash
python nombre_del_archivo.py
```

## Contenido

| Práctica | Archivos |
|---|---|
| 1.1 Entorno y primera ejecución | `hola_python.py`, `presentacion.py`, `laboratorio_de_errores.py` |
| 1.2 Variables y tipos de datos | `datos_basicos.py`, `perfil_aprendiz.py`, `inventario.py`, `error_variables.py` |
| 1.3 Operadores y expresiones | `operadores.py`, `conversion_tiempo.py`, `calculo_promedio.py`, `calculo_compra.py`, `calculo_salario.py`, `factura_simple.py` |
| 1.4 Entrada con `input()` | `saludo.py`, `tipo_entrada.py`, `prueba_entrada.py`, `datos_usuario.py`, `suma_interactiva.py`, `conversor_temperatura.py`, `salario_interactivo.py`, `programa_incompleto.py`, `conversion_unidades.py` |
| 1.5 Reto integrador | `cotizador_compra.py`, `pruebas_cotizador.py`, `cotizador_ampliado.py`, `cotizador_depuracion.py` |

## Cotizador de compra (`cotizador_compra.py`)

Solicita cliente, producto, precio unitario, cantidad, descuento (%) e impuesto (%) y muestra
subtotal, descuento, base, impuesto y total. El impuesto se aplica sobre la base (después del descuento).

```bash
python cotizador_compra.py
```

```text
Nombre del cliente: Laura
Producto: Teclado mecánico
Precio unitario: 180000
Cantidad: 2
Descuento (%): 10
Impuesto (%): 19
...
Subtotal: $360000.0
Descuento: $36000.0
Base: $324000.0
Impuesto: $61560.0
TOTAL: $385560.0
```

## Pruebas

```bash
python pruebas_cotizador.py
```

Ejecuta el cotizador con el ejemplo del enunciado y los casos 1–4 y compara con lo esperado
(180000.0, 150000.0, 300000.0 y 119000.0). Resultado actual: **5/5 casos correctos**.

## Informe

El informe en PDF está en [`informe/Informe_Laboratorio_01.pdf`](informe/Informe_Laboratorio_01.pdf).
