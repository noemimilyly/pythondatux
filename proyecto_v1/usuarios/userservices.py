
from sqlite3 import Connection
from config.email import EmailService
# llama a la libreria y trae su objecto connection

def getUser(email:str,con:Connection):
    cursor = con.cursor()
    query = "select * from user where email = ?"
    result= cursor.execute(query,email)
    data= result.fetchone()
    return data

def Login(email:str, password:str, conn:Connection):
    try:
        cursor = conn.cursor()
        query = "SELECT * FROM usuarios_sistema where email = ?"
        result = cursor.execute(query,(email,))
        result = result.fetchone()
        emailVerified = result[1]
        passwordVerified = result[2]
        typeUser = result[5]
        if password != passwordVerified:
            return False
        return {
            "user": emailVerified,
            "type_user": typeUser,
            "login": True
        }

        
    except Exception as e:
        print(e)
def WelcomeUser(email:str,emailService:EmailService):
    try:
        emailService.send_email(email,"Bienvenido",f"Bienvenido {email}")
    except Exception as e:
        print("e",e)
    
#definimos el insert user para usarlo

def insertUser(email: str, password: str, typeUser: str, conn: Connection):
    try:
        cursor = conn.cursor()
        query = """
        INSERT INTO usuarios_sistema (email, password, type_user)
        VALUES (?, ?, ?)
        """
        cursor.execute(query, (email, password, type_user))
        conn.commit()
        return True
    except Exception as e:
        print("Error al insertar usuario:", e)
        return False
