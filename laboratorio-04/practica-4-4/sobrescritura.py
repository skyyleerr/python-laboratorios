class Notificacion:
    def enviar(self): return "Enviando notificación general"
class Correo(Notificacion):
    def enviar(self): return "Enviando correo electrónico"
class MensajeTexto(Notificacion):
    def enviar(self): return "Enviando mensaje de texto"
for notificacion in [Notificacion(), Correo(), MensajeTexto()]:
    print(notificacion.enviar())
