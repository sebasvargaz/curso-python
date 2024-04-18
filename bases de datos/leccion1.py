import sqlite3 

conexion = sqlite3.connect("ejemplo.db")

cursor = conexion.cursor()

cursor.execute("CREATE TABLE usuarios (nombre VARCHAR(100), edad INTEGER, email VARCHAR(100))")
cursor.execute("INSERT INTO usuarios VALUES ('Hector', '27', 'hector@ejemplo.com')")

cursor.execute("SELECT * FROM usuarios")
usuario = cursor.fetchone()
print(usuario)
usuarios = [
    ('Mario', 51, 'marioejemplo@hotmail.com'),
    ('Sebastian', 14, 'msebasjemplo@hotmail.com'),
    ('Camila', 16, 'camilaloverso@hotmail.com'),
]

cursor.executemany("INSERT INTO usuarios VALUES (?,?,?)", usuarios)


conexion.commit()
conexion.close()