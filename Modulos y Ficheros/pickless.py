import pickle 
from io import open

class Pelicula:

    # Constructor de clase
    def __init__(self, titulo, duracion, lanzamiento):
        self.titulo = titulo
        self.duracion = duracion
        self.lanzamiento = lanzamiento
        print('Se ha creado la película:',self.titulo)

    def __str__(self):
        return '{} ({})'.format(self.titulo, self.lanzamiento)


class Catalogo:

    peliculas = []

    # Constructor de clase
    def __init__(self):
        self.cargar()

    def agregar(self,p):
        self.peliculas.append(p)
        self.guardar()

    def mostrar(self):
        if len(self.peliculas) == 0:
            print("El catálogo está vacío")
            return
        for p in self.peliculas:
            print(p)

    def cargar(self):
        fichero = open('catalogo.pckl', 'ab+')
        fichero.seek(0)
        try:
            self.peliculas = pickle.load(fichero)
        except:
            print("El fichero está vacío")
        finally:
            fichero.close()
            print("Se han cargado {} películas".format(len(self.peliculas)))

    def guardar(self):
        fichero = open('catalogo.pckl', 'wb')
        pickle.dump(self.peliculas, fichero)
        fichero.close()
        
    def __del___(self):
        self.guardar()  #Guardado automático.
        print("Se ha guardado el fichero. ")

c = Catalogo()

c.mostrar()

del (c)
 
