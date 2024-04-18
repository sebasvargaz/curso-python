import sqlite3 

def crear_bd():
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    
    try:
        cursor.execute(''' CREATE TABLE categoria(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL)''')
    except sqlite3.OperationalError:
        print("La tabla de categorías ya existe. ")
    else: 
        print("La tabla de categorías se ha creado correctamente. ")
    
    try: 
        cursor.execute('''CREATE TABLE plato(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(100) UNIQUE NOT NULL,
            categoria_id INTEGER NOT NULL,
            FOREIGN KEY(categoria_id) REFERENCES categoria(id))''')
    except sqlite3.OperationalError:
        print("La tabla de Platos ya existe. ")
    else: 
        print("La tabla de Platos se ha creado correctamente. ")
    
    conexion.close()

def agregar_categoria():
    categoria = input("Ingrese el nombre de la nueva categoría: \n> ")
    conexion = sqlite3.connect("restaurante.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO categoria VALUES (null, '{}')".format(categoria))
    
    except sqlite3.IntegrityError:
        print("La categoría '{}' ya existe".format(categoria))
    else:
        print("Catergoría creada correctamente. ")
        
    conexion.commit()
    conexion.close()

def agregar_plato():
        conexion = sqlite3.connect("restaurante.db")
        cursor = conexion.cursor()
        
        categorias = cursor.execute("SELECT * FROM categoria").fetchall()
        print("Seleccione una categoría para añadir el plato: ")
        for categoria in categorias:
            print("[{}] {}".format(categoria[0], categoria[1]))
            
        categoria_usuario = int(input("> "))
        plato = input("Ingrese el nombre del nuevo plato: \n> ")
                 
        try:
            cursor.execute("INSERT INTO plato VALUES (null, '{}',{})".format(plato, categoria_usuario))
    
        except sqlite3.IntegrityError:
            print("El plato '{}' ya existe".format(plato))
        else:
            print("Plato '{}' creado correctamente.".format(plato))    
            
        conexion.commit()
        conexion.close()
    
def mostrar_menu():
        conexion = sqlite3.connect("restaurante.db")
        cursor = conexion.cursor()
        categorias = cursor.execute("SELECT * FROM categoria").fetchall()  
        for categoria in categorias:
            print(categoria[1])
            platos = cursor.execute("SELECT * FROM plato WHERE categoria_id={}".format(categoria[0])).fetchall()
            for plato in platos:
                print("\t{}".format(plato[1])) 
        conexion.close()

crear_bd() 

#menu

while True:
    print("________________________________________")
    print("\nBienvenido al gestor del restaurante! ")
    opcion = input ("\nIntroduce una opción: \n1. Agregar una categoría.\n2. Agregar plato.\n3. Mostrar menú\n4. Salir del programa.\n\n> ")
    
    if opcion == '1':
        agregar_categoria()
    elif opcion == '2':
        agregar_plato()
    elif opcion == '3':
        mostrar_menu()
    elif opcion == '4':
        print("Bye")
        break
    else:
        print ("Opción incorrecta. ")
        



 