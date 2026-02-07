from config.config import ConfigBd
from usuarios.userservices import insertUser

config = ConfigBd()
conn = config.bd

insertUser(
    email="mimipz15038@gmail.com",
    password="1234",
    typeUser="admin",
    conn=conn
)

print("Usuario creado correctamente")
