import Libreria_ampliada
def probabilidad(posicion, vector):
    total =0
    for i in vector:
        total = total + (i[0]**2 + i[1]**2)
    total = total**0.5

    
    res = (vector[posicion][0]**2 + vector[posicion][1]**2)/total**2
    return res
def pureba1():
    for i in range(10):
        print(100*probabilidad(i,vecto1),i)
def bra(vecto):
    for i in range(len(vecto2)):
        vecto[i][1]= vecto2[i][1]*-1
    return vecto

def normalizar(vector):
    total =0
    for i in vector:
        total = total + (i[0]**2 + i[1]**2)
    total=total**0.5
    for i in range(len(vector)):
        vector[i][0]= vector[i][0]/total
        vector[i][1]= vector[i][1]/total
    return vector
def amplitud(vec,vec2):
    vec= normalizar(vec)
    vec2=normalizar(vec2)
    vec2=bra(vec2)
    produc=ProductoInterno(vec2,vec)
    return produc

