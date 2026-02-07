# servicio/propiedades.py
# Funciones simples para manejar propiedades

def listar_propiedades(conn):
    """Lista todas las propiedades de la base de datos"""
    cursor = conn.cursor()
    
    # Query simple para obtener propiedades
    cursor.execute('''
        SELECT id_producto, codigo_producto, titulo, tipo_propiedad, 
               direccion, precio, estado
        FROM productos
    ''')
    
    propiedades = cursor.fetchall()
    
    # Mostrar las propiedades
    print("\n" + "="*80)
    print("LISTADO DE PROPIEDADES")
    print("="*80)
    
    if not propiedades:
        print("No hay propiedades registradas")
    else:
        for prop in propiedades:
            print(f"\nID: {prop[0]}")
            print(f"Código: {prop[1]}")
            print(f"Título: {prop[2]}")
            print(f"Tipo: {prop[3]}")
            print(f"Dirección: {prop[4]}")
            print(f"Precio: S/. {prop[5]:,.2f}")
            print(f"Estado: {prop[6]}")
            print("-" * 80)
    
    print(f"\nTotal de propiedades: {len(propiedades)}")
    print("="*80)
    
    return propiedades


def listar_clientes(conn):
    """Lista todos los clientes de la base de datos"""
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT id_cliente, nombre, apellido, email, telefono, documento, estado
        FROM clientes
    ''')
    
    clientes = cursor.fetchall()
    
    print("\n" + "="*80)
    print("LISTADO DE CLIENTES")
    print("="*80)
    
    if not clientes:
        print("No hay clientes registrados")
    else:
        for cliente in clientes:
            print(f"\nID: {cliente[0]}")
            print(f"Nombre: {cliente[1]} {cliente[2]}")
            print(f"Email: {cliente[3]}")
            print(f"Teléfono: {cliente[4]}")
            print(f"Documento: {cliente[5]}")
            print(f"Estado: {cliente[6]}")
            print("-" * 80)
    
    print(f"\nTotal de clientes: {len(clientes)}")
    print("="*80)
    
    return clientes
