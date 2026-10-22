# Cálculo manual
# Producto	Operación	    Valor
# Teclados	$85.000 × 4	    $340.000
# Mouse 	$45.000 × 7	    $315.000
# Monitores	$700.000 × 2	$1.400.000
# Total		                $2.055.000

productos = [
    {"codigo": "P001", "nombre": "Teclado", "precio": 85000.0, "cantidad": 4},
    {"codigo": "P002", "nombre": "Mouse", "precio": 45000.0, "cantidad": 7},
    {"codigo": "P003", "nombre": "Monitor", "precio": 700000.0, "cantidad": 2}
]

valor_inventario = 0

for producto in productos:
    valor_inventario += producto["precio"] * producto["cantidad"]

print("Valor del inventario:", valor_inventario)

# C:\Users\Asus\Downloads\python-laboratorio-02>C:\Users\Asus\AppData\Local\Programs\Python\Python315\python.exe c:/Users/Asus/Downloads/python-laboratorio-02/valor_inventario.py
# Valor del inventario: 2055000.0