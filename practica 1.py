msg = """ 
Bienvenido al menú de inicio seleccione un numero del 1 al 5 equivalente a las siguientes opciones:
Opcion 1 (1) : Sumar 2 numeros
Opcion 2 (2) : Crea una coleccion de productos para un mercado
Opcion 3 (3) : Agrega un nuevo producto a la coleccion
Opcion 4 (4) : Mostrar el producto de precio mas bajo
Opcion 5 (5) : Salir del programa
"""
productos = []
def sumar():
    a=int(input("ingrese el primer numero:" ))
    b=int(input("ingrese el segundo numero:"))
    print(f"la suma es:{a+b}")
def crear_coleccion():
    productos.clear()
    cantidad_productos=int(input("¿Cuantos productos desea ingresar?: "))
    for i in range (cantidad_productos):
        nombre=input(f"ingrese el nombre del producto # {i+1}:")
        precio=float(input(f"ingrese el precio del producto (soles) # {i+1}:"))
        while precio <= 0:
            print("el valor ingresado es invalido, ya que el precio es positivo")
            precio= float(input("ingrese el precio correctamente:"))
        productos.append({"nombre": nombre, "precio": precio})
    print ("se creo la colección correctamente")
def agregar_producto():
    if not productos:
        print("usted no tiene ninguna colección creada, cree una primera para poder agregar productos")
    else:
        nombre=input("ingrese el nombre del producto que desea agregar")
        precio=float(input("ingrese el precio (en soles) del producto que desea agregar"))
        while precio <= 0:
            print("el valor ingresado es invalido, ya que el precio es positivo")
            precio= float(input("ingrese el precio correctamente:"))
        productos.append({"nombre": nombre, "precio": precio})
def producto_mas_barato():
    if not productos:
        print("No hay productos registrados")
    else:
        menor = productos[0]
        for p in productos:
            if p["precio"] < menor["precio"]:
                menor = p
        print(f"El producto mas barato es: {menor['nombre']} y su precio es {menor['precio']}")
opcion = 0
while opcion != 5:
    opcion=int(input(msg))
    if opcion == 1:
        sumar()
    elif opcion == 2:
        crear_coleccion()
    elif opcion == 3:
        agregar_producto()
    elif opcion == 4:
        producto_mas_barato()
    elif opcion == 5:
        print("Saliendo del programa...")
        break
    else:
        print("Opción invalida, porfavor seleccione correctamente")
    print("volviendo al menu de inicio......")






        
             
