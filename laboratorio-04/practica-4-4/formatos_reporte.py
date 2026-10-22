class ReporteTexto:
    def generar(self, datos):
        return "Registros: " + "; ".join(str(dato) for dato in datos)
class ReporteResumen:
    def generar(self, datos):
        return f"Cantidad de registros: {len(datos)}"
datos = ["Teclado", "Mouse", "Monitor"]
for reporte in [ReporteTexto(), ReporteResumen()]:
    print(reporte.generar(datos))
