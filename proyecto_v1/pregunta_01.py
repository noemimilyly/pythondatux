# Pregunta 1
import sqlite3

EMAIL = 'mimipz15038@gmail.com'
PASSWORD = 'puppy15038'
NOMBRE = 'Noemi'
APELLIDO = 'Perez' 
TIPO = 'admin' # puede ser 'admin' o 'ventas'

conn = sqlite3.connect('bd-si.db')
cursor = conn.cursor()

cursor.execute('''
    INSERT INTO usuarios_sistema (email, password, nombre, apellido, tipo_usuario, estado)
    VALUES (?, ?, ?, ?, ?, 1)
''', (EMAIL, PASSWORD, NOMBRE, APELLIDO, TIPO))  

# Guardar cambios
conn.commit()
print("Usuario agregado correctamente")
print(f"Email: {EMAIL}")
print(f"Password: {PASSWORD}")

# Verificar que se insertó
cursor.execute("SELECT * FROM usuarios_sistema WHERE email = ?", (EMAIL,))
usuario = cursor.fetchone()
print("\nUsuario en la BD:", usuario)
conn.close()
