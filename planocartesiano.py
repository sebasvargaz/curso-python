import math 


class Punto:
    
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({},{})".format(self.x, self.y)
    
    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} Es el primer cuadrante! ".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} Es el segundo cuadrante! ".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} Es el tercer cuadrante! ".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} Es el cuarto cuadrante! ".format(self))
        else:
            print("{} Se encuentra sobre el origen".format(self))
    
    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(self, p, p.x - self.x, p.y - self.y))
        
    def distancia(self, p):
        d = math.sqrt((p.x - self.x)**2 + (p.y - self.y)**2)
        print("La distancia entre los puntos {} y {} es {}".format(self, p, d))
        

A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

# A.cuadrante()
# C.cuadrante()
# D.cuadrante()

#A.vector(B)
#B.vector(A)

A.distancia(B)
B.distancia(A)

