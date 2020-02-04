# CNYT
# Autor : Lorenzo Marquez Pinto
# fecha : 27/01/2020
Esta es una libreria realizada en python para las siguientes operaciones entre números complejos:
- Suma
- Producto
- Resta
- División
- Módulo
- Conjugado
- Conversión entre representaciones polar y cartesiano
- Retornar la fase de un número complejo.
# Así se hace la suma:
~~~ 
  def suma(comple1,comple2):
   """pre entran dos numeros complejos
      pos sale el resultado de la suma entre 2 numeros complejos"""
   comple3 = (comple1[0]+comple2[0],comple1[1]+comple2[1])
   return comple3 
~~~
