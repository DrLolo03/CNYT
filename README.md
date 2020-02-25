# CNYT
# Autor : Lorenzo Marquez Pinto
# fecha : 22/02/2020
# Libreria de Complejos, Matrices y Vectores
En esta libreria se van a trabajar numeros complejos como las operaciones que se pueden hacer con estos y tambien se trabajara con matrices y vectores compuestos de complejos y sus operaciones mas comunes y manejadas para el curso de CNYT de la Escuela Colombiana de Ingenieria
# Pre-Requisitos
Para poder usar esta libreria se necesita una herramienta que lea/corra Python  
# Instalacion
 En caso de no tener python https://www.python.org/downloads/release/python-381/ se puede descargar del anterior enlace.
 -En el enlace en la parte de abajo se podran ver varias versiones de python segun las especificaciones de su computador ( 32 o 64 bits)
 -Escojer la correspondiente a su computador
 -Descargar la version escogida
 -una vez descargada instalarla segun lo indique el instalador y siguiendo las recomendaciones que tiene

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
# Así se hace la matriz conjugada:
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
# Pruebas
Para ejecutar las pruebas correspondientes se deben tener todos los archivos del repositorio descargados ya que unos se llaman a otros para poder ejectuar las pruebas.
Ejemplo:
De la libreria "Libreria_ampliada" tomo este fracmento de codigo 
~~~ 
import math
from Complejos import *
def RestaVecto(vec1, vec2):
   """pre entran dos vectores complejos
      pos sale el resultado de la resta entre 2 vectores complejos"""
   if (len( vec1)==len( vec2)):
      for x in range(len( vec1)):
         vec1[x] = resta( vec1[x],vec2[x])
      return vec1
~~~ 
y su prueba correspondiente seria
~~~ 
import unittest
from Libreria_ampliada import *
a = [1,1]
b = [2,2]
c = [3,3]
d = [7,8]
 def testRestaVector(self):
        self.assertEqual(RestaVecto([a,b],[a,b]), [(0,0),(0,0)] )
        self.assertEqual(RestaVecto([a,c],[c,b]), [(-2,-2),(1,1)])
~~~ 
En ambos se ve la importancia de tener todos los archivos descargados en la misma carpeta ya que como se ve estos son utilizados por otras librerias y lo que se hace en la prueba es se da unos datos y se llama a la funcion y el resultado de esa funcion se compara con la respuesta correcta para verificar que sean iguales 

# Construido con:
Las librerias fueron construidas en el IDLE de python y en JETBRAINS PYCHARM de las ultimas versiones hasta la fecha(24/02/2020)
# Licencia
Este proyecto esta bajo Licencia de uso libre https://github.com/DrLolo03/CNYT/blob/master/LICENSE para mas informacion
