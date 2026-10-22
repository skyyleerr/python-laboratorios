edad = int(input("Edad: "))
autorizacion = input("¿Tiene autorización? (si/no): ").strip().lower()

if edad >= 18:
    print("Acceso permitido.")
elif autorizacion == "si":
    print("Acceso permitido.")
else:
    print("Acceso no permitido.")
    
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python acceso_sala.py
# Edad: 20
# ¿Tiene autorización? (si/no): no
# Acceso permitido.
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python acceso_sala.py              
# Edad: 17
# ¿Tiene autorización? (si/no): si
# Acceso permitido.
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python acceso_sala.py
# Edad: 17
# ¿Tiene autorización? (si/no): no
# Acceso no permitido.
# PS C:\Users\ProgacionSena\Desktop\python-laboratorio-02> python acceso_sala.py
# Edad: 18
# ¿Tiene autorización? (si/no): no
# Acceso permitido.