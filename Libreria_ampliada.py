import math
from Complejos import *

def RestaVecto(vec1, vec2):
   """pre entran dos vectores complejos
      pos sale el resultado de la resta entre 2 vectores complejos"""
   if (len( vec1)==len( vec2)):
      for x in range(len( vec1)):
         vec1[x] = resta( vec1[x],vec2[x])
      return vec1


def VectorR(vect1, vect2):
   tam = len(vect1)
   if (tam == len(vect2)):
      for x in range(tam):
         vect1[x] = resta(vect1[x], vect2[x])
      return vect1

def SumaVecto(vec1, vec2):
   """pre entran dos vectores complejos
      pos sale el resultado de la suma entre 2 vectores complejos"""
   if (len( vec1)==len( vec2)):
      for x in range(len( vec1)):
         vec1[x]=suma(vec1[x],vec2[x])
      return vec1

def InversaVector( vector):
   """pre entran un vector complejo
      pos sale el resultado de la inversa de un vector complejo"""
   for x in range(len(vector)):
      valor = vector[x]
      vector[ x ] = conjugada(valor)
      vector[ x ][ 0 ] = - valor[0]
   return vector
def EscalarVector( vector, comple):
   """pre entran un vector y un complejo
      pos sale el resultado del producto escalar de un vector y un complejo"""
   for x in range(len( vector)):
      vector[ x ] = multip( comple, vector[ x ] )
   return vector
def SumaMatriz( mat1, mat2 ):
   """pre entran dos matrices
      pos sale el resultado de la suma de ambas matrices"""
   if len(mat1)==len(mat2) and len(mat1[0])==len(mat2[0]):
      for i in range(len( mat1 )):
         for j in range(len( mat1[ 0 ] )):
            mat1[ i ][ j ] = suma(mat1[i][j], mat2[i][j])

      return mat1
def InversaMatriz( mat ):
   """pre entran una matriz
      pos sale el resultado de la inversa de la matriz"""
   for i in range(len(mat)):
      mat[ i ] = InversaVector(mat[i])
   return mat

def MultipEscalarMatriz( comple, mat ):
   """pre entran una matriz y un complejo
      pos sale el resultado del producto escalar de un matriz y un complejo"""
   for i in range(len(mat)):
      for j in range(len(mat[0])):
         mat[ i ][ j ] = multip( comple, mat[ i ][ j ] )

   return mat

def MatTranspuesta( mat ):
   """pre entran una matriz 
      pos sale el resultado de la matriz transpuesta"""
   if ( type( mat[ 0 ][ 0 ] ) is int ):
      return mat
   res  = [["" for k in range(len( mat))] for p in range(len(mat[0]))]
   for i in range(len( mat[ 0 ] ) ):
      for j in range(len( mat)):
         res[ i ][ j ] = mat[ j ][ i ]

   return res

def MatrizAdjunta(mat):
   """pre entran una matriz 
      pos sale el resultado de la matriz adjunta"""
   res  = MatrizConjugada(MatTranspuesta(mat) )
   return res

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
def MatrizMultip( mat1, mat2 ):
   """pre entran dos matrices 
      pos sale el resultado de multiplicarlas """
   row1, col1 = len( mat1 ),len( mat1[ 0 ] )
   row2, col2 =  len( mat2 ), len( mat2[ 0 ] )
   if ( len( mat1 ) ==len( mat2 )):
      res = [ [  ( 0,0 )  for t in range( len( mat2[ 0 ] )) ] for x in range(len( mat1 )) ]
      for i in range(len( mat1 ) ):
         for j in range(len(mat2[0])):
            valor = ( 0, 0 )
            for k in range(len(mat2[0])):
               mult =  multip( mat1[ i ][ k ], mat2[ k ][ j ]  )
               valor =  suma( valor , mult )
               res[ i ][ j ]  = valor
      return res
   else:
      return None
def ProductoInterno( vector1 , vector2 ):
   """pre entran dos vectores 
      pos sale el resultado de su producto interno """
   res = [ 0, 0 ]
   for x in range( len( vector1 ) ):
      res = suma( res, multip( vector1[ x ],vector2[x]))
   return res

def VectorNormal( vector  ):
   """pre entran un vector 
      pos sale el resultado de la Norma de un vector """
   res  = math.sqrt(abs(ProductoInterno( vector, vector )[ 0 ] ) )
   return res
def DistanciaVector( vector1, vector2 ):
   """pre entran dos vectores 
      pos sale el resultado de la distancia entre estos """
   res = VectorNormal( VectorR( vector1, vector2) )
   return res

def MatrizIdentidad( mat ):
   """pre entra una matriz
      pos sale el resultado de la identidad de la matriz """
   mat=[[[] for i in range(len(mat[0]))] for j in range(len(mat))]
   for i in range(len(mat)):
      for j in range(len(mat[0]) ):
         if i==j:
            mat[ i ][ j ] =  [ 1,0]
         else:
            mat[ i ][ j ] =  [ 0,0 ]
   return mat

def Unitaria( mat ):
   """pre entra una matriz
      pos sale el resultado de su matirz unitaria """
   if len(mat)== len(mat[0]) :
      adjunta = MatrizAdjunta(mat)
      return (MatrizMultip(mat ,adjunta) == MatrizIdentidad(mat)) and (MatrizMultip(mat,adjunta) == MatrizMultip(adjunta , mat))
   else:
      return False
def Hermitania(mat):
   """pre entra una matriz
      pos sale la validacion que verifico si es o no es hermitania """
   res = MatrizAdjunta(mat)
   return  str( res ) == str( mat )
