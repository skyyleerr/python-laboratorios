class Notificacion:
    def enviar(self, mensaje): raise NotImplementedError
class NotificacionCorreo(Notificacion):
    def enviar(self, mensaje): return f"Correo enviado: {mensaje}"
class NotificacionConsola(Notificacion):
    def enviar(self, mensaje): return f"Consola: {mensaje}"
for notificacion in [NotificacionCorreo(), NotificacionConsola()]:
    print(notificacion.enviar("Inventario actualizado"))
