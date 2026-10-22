"""Interfaz de consola; input() y mensajes permanecen en este módulo."""
import math
from almacenamiento import RUTA_JSON, ErrorAlmacenamiento, cargar_inventario, guardar_inventario
from inventario import Inventario
from producto import CATEGORIAS, Producto
from reportes import exportar_csv


def convertir_precio(texto):
    texto = texto.strip().replace("$", "").replace(" ", "")
    if "," in texto:
        texto = texto.replace(".", "").replace(",", ".")
    elif "." in texto:
        partes = texto.split(".")
        if len(partes) > 2 or (len(partes) == 2 and len(partes[1]) == 3):
            texto = texto.replace(".", "")
    return float(texto)


def leer_texto(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato: return dato
        print("Este campo es obligatorio.")


def leer_entero(mensaje, minimo=0):
    while True:
        try: valor = int(input(mensaje))
        except ValueError:
            print("Escribe un número entero.")
            continue
        if valor < minimo:
            print(f"El valor debe ser como mínimo {minimo}.")
            continue
        return valor


def leer_precio():
    while True:
        try: precio = convertir_precio(input("Precio: "))
        except ValueError:
            print("Escribe un precio válido (ej.: 85000, 85.000 o 85.000,50).")
            continue
        if not math.isfinite(precio) or precio <= 0:
            print("El precio debe ser finito y mayor que cero.")
            continue
        return precio


def mostrar_menu():
    print("\n================================")
    print("       GESTOR DE INVENTARIO")
    print("================================")
    for linea in ("1. Registrar producto", "2. Listar productos", "3. Buscar por código",
                  "4. Actualizar existencias", "5. Eliminar producto",
                  "6. Consultar productos sin stock", "7. Resumen del inventario",
                  "8. Guardar inventario", "9. Exportar reporte CSV", "0. Salir"):
        print(linea)


def mostrar_producto(p):
    print(f"{p.codigo} - {p.nombre} - {p.categoria} - ${p.precio} - "
          f"{p.cantidad} unidades - valor ${p.calcular_valor()}")


def ejecutar(inventario=None, solo_lectura=False):
    inventario = inventario or Inventario()
    if solo_lectura:
        print("AVISO: archivo persistente inválido. Modo de solo consulta; no se guardará sobre el archivo.")
    while True:
        mostrar_menu()
        opcion = input("Opción: ").strip()
        try:
            if opcion == "1":
                if solo_lectura: print("Operación bloqueada hasta resolver el archivo JSON."); continue
                codigo = leer_texto("Código: ").upper()
                nombre = leer_texto("Nombre: ")
                categoria = leer_texto(f"Categoría {CATEGORIAS}: ")
                precio = leer_precio()
                cantidad = leer_entero("Cantidad: ")
                producto = Producto(codigo, nombre, categoria, precio, cantidad)
                if not inventario.registrar_producto(producto):
                    print("Ya existe ese código."); continue
                print("Producto registrado.")
                try: print("Guardado en:", guardar_inventario(inventario))
                except OSError as error: print("No se pudo guardar; el cambio queda solo en memoria:", error)
            elif opcion == "2":
                productos = inventario.listar_productos()
                if not productos: print("No hay productos registrados.")
                for producto in productos: mostrar_producto(producto)
            elif opcion == "3":
                producto = inventario.buscar_producto(input("Código: "))
                mostrar_producto(producto) if producto else print("Producto no encontrado.")
            elif opcion == "4":
                if solo_lectura: print("Operación bloqueada hasta resolver el archivo JSON."); continue
                codigo = leer_texto("Código: ").upper()
                if inventario.buscar_producto(codigo) is None: print("Producto no encontrado."); continue
                cantidad = leer_entero("Nueva cantidad: ")
                inventario.actualizar_existencias(codigo, cantidad)
                print("Existencias actualizadas.")
                try: print("Guardado en:", guardar_inventario(inventario))
                except OSError as error: print("No se pudo guardar; el cambio queda solo en memoria:", error)
            elif opcion == "5":
                if solo_lectura: print("Operación bloqueada hasta resolver el archivo JSON."); continue
                codigo = leer_texto("Código: ").upper()
                if not inventario.eliminar_producto(codigo): print("Producto no encontrado."); continue
                print("Producto eliminado.")
                try: print("Guardado en:", guardar_inventario(inventario))
                except OSError as error: print("No se pudo guardar; el cambio queda solo en memoria:", error)
            elif opcion == "6":
                agotados = inventario.productos_sin_stock()
                if not agotados: print("No hay productos sin stock.")
                for producto in agotados: mostrar_producto(producto)
            elif opcion == "7":
                r = inventario.resumen()
                print("Productos registrados:", r["productos_registrados"])
                print("Unidades disponibles:", r["unidades_disponibles"])
                print("Valor del inventario: $" + str(float(r["valor_total"])))
                categorias = sorted(r["categorias"])
                print("Categorías utilizadas:", len(categorias), categorias)
            elif opcion == "8":
                if solo_lectura: print("Guardado bloqueado para proteger el archivo inválido."); continue
                print("Guardado en:", guardar_inventario(inventario))
            elif opcion == "9":
                print("Reporte exportado:", exportar_csv(inventario))
            elif opcion == "0":
                if not solo_lectura:
                    try: print("Estado final guardado en:", guardar_inventario(inventario))
                    except OSError as error: print("No se pudo guardar al salir:", error)
                print("Programa finalizado.")
                break
            else: print("Opción no válida.")
        except (ValueError, TypeError) as error:
            print("Datos rechazados:", error)
        except OSError as error:
            print("Error de archivo:", error)


def main():
    try:
        inventario = cargar_inventario()
    except ErrorAlmacenamiento as error:
        print("No fue posible cargar el inventario:", error)
        ejecutar(Inventario(), solo_lectura=True)
    else:
        print("Productos recuperados:", len(inventario.listar_productos()))
        ejecutar(inventario)

if __name__ == "__main__":
    main()
