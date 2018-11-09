#Importamos modelado 
from mipaquete.modelado import *
#creamos un objeto tipo empleado para presentar los datos de la primera clase
e = Empleado()
e.agregar_nombre("luis")
e.agregar_apellido("Benitez")
e.agregar_cedula("1110001")
print(e.presentar_datos())

#creamos un objeto EmpleadoPorHoras para presentar los datos de la segunda clase
e1 = EmpleadoPorHoras()
nombre = input("Ingrese su nombre:\n")
e1.agregar_nombre(nombre)
e1.agregar_apellido("Andrade")
e1.agregar_cedula("1110001")
e1.agregar_numero_horas(15)
e1.agregar_valor_horas(20.2)
print(e1.presentar_datos())

#Creamos un objeto EmpleadoFijo para presentar los datos de la tercera clase
e2 = EmpleadoFijo()
e2.agregar_sueldo(300.2)
e2.agregar_descuento_seguro(10)
#Se agrega solicita al usuario que ingrese un valor a la variable comision
comision = input("Ingrese Comision: \n")
#Se procede a transformar comision a una variable tipo float
comision = float(comision)
e2.agregar_comision_fija(comision)
e2.nombre = "Ana"
e2.apellido = "Diaz"
e2.cedula = "1110001"
print(e2.presentar_datos())

#Se crea un objeto EmpleadoPorSemana para presentar los datos de la cuarta clase 
e3 = EmpleadoPorSemana()
e3.agregar_semanas(3)
e3.agregar_valor_semanas(30.2)
e3.nombre ="Miguel"
e3.apellido = "Caceres"
e3.cedula = "1110001"
print(e3.presentar_datos())