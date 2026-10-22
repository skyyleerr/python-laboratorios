compra = float(input("Valor de la compra: "))

if compra >= 200000:
    envio = 0
elif compra >= 100000:
    envio = 10000
else:
    envio = 18000

total = compra + envio

print("Valor de la compra:", compra)
print("Costo del envío:", envio)
print("Total a pagar:", total)

# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python costo_envio.py
# Valor de la compra: 99999
# Valor de la compra: 99999.0
# Costo del envío: 18000
# Total a pagar: 117999.0
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python costo_envio.py
# Valor de la compra: 100000
# Valor de la compra: 100000.0
# Costo del envío: 10000
# Total a pagar: 110000.0
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python costo_envio.py
# Valor de la compra: 199999 
# Valor de la compra: 199999.0
# Costo del envío: 10000
# Total a pagar: 209999.0
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python costo_envio.py
# Valor de la compra: 200000
# Valor de la compra: 200000.0
# Costo del envío: 0
# Total a pagar: 200000.0

''''''

# = → asigna un valor.
# == → compara dos valores.
# Indentación: indica qué instrucciones pertenecen a un if, elif o else.