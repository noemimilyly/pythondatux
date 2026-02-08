from config.email import EmailService

# Crear instancia del servicio
email_service = EmailService()

# Enviar correo  simple
resultado = email_service.send_email(
    to_email="mimipz15038@gmail.com",
    subject="Prueba de Sistema DATUX",
    message="Hola, este es un mensaje de prueba del sistema inmobiliario DATUX, no responder este correo por favor"
)

# Validar si se envió correctamente
if resultado:
    print("Correo enviado exitosamente")
else:
    print("Error al enviar correo")
