#Lorenzo marquez , 16/01/2020
from sys import stdin
import math
def suma(comple1,comple2):
   """pre entran dos numeros complejos
      pos sale el resultado de la suma entre 2 numeros complejos"""
   comple3 = (comple1[0]+comple2[0],comple1[1]+comple2[1])
   return comple3
def resta(comple1,comple2):
   """pre entran dos numeros complejos
      pos sale el resultado de la resta entre 2 numeros complejos"""
   comple3 = (comple1[0]-comple2[0],comple1[1]-comple2[1])
   return comple3
def multip(compl1,compl2):
   """pre entran dos numeros complejos
      pos sale el resultado de la multiplicacion entre 2 numeros complejos"""
   comple3 = (compl1[0]*compl2[0]-compl1[1]*compl2[1],compl1[0]*compl2[1]+compl1[1]*compl2[0])
   return comple3
def div(compl1,compl2):
   """pre entran dos numeros complejos
      pos sale el resultado de la divicion entre 2 numeros complejos"""
   comple3 = ((compl1[0]*compl2[0] + compl2[1]*compl1[1])/(compl2[0]**2 + compl2[1]**2),(compl2[0]*compl1[1] - compl1[0]*compl2[1])/(compl2[0]**2 + compl2[1]**2))
   return comple3
def moodule(comple1):
   """pre entra un numero complejo
      pos sale el resultado del modulo de un numero complejo"""
   comple3 = (comple1[0]**2 + comple1[1]**2)**0.5
   return comple3
def cartpol(comple1):
   """pre entra un numero complejo
      pos sale el resultado del pasar esa posicion cartesiana a polar de la entrada"""
   d=0
   if comple1[0]<0 and comple1[1]>0:
      d= math.pi
   elif comple1[0]<0 and comple1[1]<0:
      d= math.pi
   coor = ((comple1[0]**2 + comple1[1]**2)**0.5,math.atan(comple1[1]/comple1[0])+d)
   return coor
def fase(comple1):
   """pre entra un numero complejo
      pos sale el resultado del pasar esa posicion cartesiana retorna la fase de esa posicion (el angulo)"""
   d=0
   if comple1[0]<0 and comple1[1]>0:
      d= math.pi
   elif comple1[0]<0 and comple1[1]<0:
      d= math.pi
   return math.atan(comple1[1] / comple1[0]) + d    
def conjugada(comple1):
   """pre entra un numero complejo
      pos sale el resultado del conjugado de un numero complejo"""
   answ = [comple1[ 0 ],-comple1[ 1 ]]
   return answ
