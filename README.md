# CNYT
# Autor : Lorenzo Marquez Pinto
# fecha : 22/02/2020
La primera libreria "Complejos" realizada en python se hizo para las siguientes operaciones entre números complejos:
- Suma
- Producto
- Resta
- División
- Módulo
- Conjugado
- Conversión entre representaciones polar y cartesiano
- Retornar la fase de un número complejo.
# Así se hace la suma de complejos:
~~~ 
  def suma(comple1,comple2):
   """pre entran dos numeros complejos
      pos sale el resultado de la suma entre 2 numeros complejos"""
   comple3 = (comple1[0]+comple2[0],comple1[1]+comple2[1])
   return comple3 
~~~
La segunda Libreria "Libreria_ampliada" realiza las siguientes operaciones 
- Adición de vectores complejos.
- Inverso (aditivo) de un vector complejo.
- Multiplicación de un escalar por un vector complejo.
- Adición de matrices complejas.
- Inversa (aditiva) de una matriz compleja.
- Multiplicación de un escalar por una matriz compleja.
- Transpuesta de una matriz/vector
- Conjugada de una matriz/vector
- Adjunta (daga) de una matriz/vector
- Producto de dos matrices (de tamaños compatibles)
- Función para calcular la "acción" de una matriz sobre un vector.
- Producto interno de dos vectores
- Norma de un vector
- Distancia entre dos vectores
- Revisar si una matriz es unitaria
- Revisar si una matriz es Hermitiana
- Producto tensor de dos matrices/vectores
# Así se revisa si una matriz es unitaria:
~~~ 
def MatrizConjugada(mat):
   """pre entran una matriz 
      pos sale el resultado de la matriz conjugada"""
   if (type( mat[ 0 ][ 0 ])is int):
      for x in range(len(mat)):
         mat[ x ] = conjugada(mat[x])
         return mat

   for i in range(len( mat )):
      for j in range(len( mat [ 0 ] )):
         mat[ i ][ j ] = conjugada( mat[ i ][ j ] )

   return mat
~~~ 
