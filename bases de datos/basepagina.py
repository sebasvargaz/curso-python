import sqlite3 

conexion = sqlite3.connect("usuarios.db")
cursor = conexion.cursor()

cursor.execute('''
    CREATE TABLE usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        nombre VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE,
        password NOT NULL 
    )
     ''')

# usuarios = [
#    ('Sebastian', 'sebasvargaz@hotmail.com', '12345')
#    ('Juan', 'sebasvargaz@hotmail.com', '12345')
# ]  
# cursor.executemany("INSERT INTO usuarios VALUES (null, ?,?,?)", usuarios)

conexion.commit()
conexion.close()
