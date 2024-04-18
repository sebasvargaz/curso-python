from io import open 


texto = "Una línea con texto\nOtra linea con texto"

fichero = open('fichero.txt','r')
fichero.seek(10)
l = fichero.read()
print (l)
fichero.close()




