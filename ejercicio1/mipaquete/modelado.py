#Empleado va a ser la clase padre de nuestras demas variables de esta es donde obtenedremos la informacion base del usuario como nombre, cedula, apellido y comision fija
class Empleado(object):

	def __init__(self):
		self.nombre = ""
		self.apellido = ""
		self.cedula = ""
		self.comision_fija = 0
#Creamos los get y sets de cada variable
	def agregar_nombre(self,nombre):
		self.nombre = nombre
	
	def obtener_nombre(self):
		return self.nombre
	
	def agregar_apellido(self,apellido):
		self.apellido = apellido
	
	def obtener_apellido(self):
		return self.apellido
	
	def agregar_cedula(self,cedula):
		self.cedula = cedula
	
	def obtener_cedula(self):
		return self.cedula
	
	def agregar_comision_fija(self,comision):
		self.comision_fija = comision
	
	def obtener_comision_fija(self):
		return self.comision_fija
#Se crea un metodo presentar datos en el cual se presentara mediante una cadena la informacion que se obtendra de la clase run  	
	def presentar_datos(self):
		cadena = "Informacion de %s %s es:\nCedula: %s\nComision fija: %d" % (self.obtener_nombre(),self.obtener_apellido(),self.obtener_cedula(),self.obtener_comision_fija())
		return cadena


class EmpleadoPorHoras(Empleado):
#llamamos los metodos de la anterior clase mediante un super aparte declaramos las variables que se usaran dentro de esta clase 

	def __init__(self):
		super(EmpleadoPorHoras,self).__init__()
		self.numero_horas = 0
		self.valor_horas = 0
		self.sueldo_final = 0
#Creamos los sets y gets de cada variable 	
	def agregar_numero_horas(self,n_horas):
		self.numero_horas = n_horas	
	
	def obtener_numero_horas(self):
		return self.numero_horas 
	
	def agregar_valor_horas(self,v_horas):
		self.valor_horas = v_horas
	
	def obtener_valor_horas(self):
		return self.valor_horas
#Calculamos el valor de el sueldo final 	
	def calcular_valor_sueldo_final(self):
		self.sueldo_final = self.obtener_valor_horas()*self.obtener_numero_horas()
		return self.sueldo_final
#Presentamos la informacion de los metodos de la calse empleado(del metodo "presentar_datos") ademas de presentar la informacion de las variables propias de esta clase	
	def presentar_datos(self):
		cadena = "%s\nNumero de horas: %d\nValor de las horas: %d\nSueldo : %f\n"%(super(EmpleadoPorHoras,self).presentar_datos(),self.obtener_numero_horas(),self.obtener_valor_horas(),self.calcular_valor_sueldo_final())
		return cadena


class EmpleadoFijo(Empleado):
#Nuevamente usamos un super para obtener los metodos de la primera clase aparte de declarar las variables propias de esta
	def __init__(self):
		super(EmpleadoFijo,self).__init__()
		self.sueldo = 0.0
		self.descuento = 0
		self.descuento_final = 0.0
		self.sueldo_final = 0.0
#Creamos los respectivos get y sets de cada variable 	
	def agregar_sueldo(self,s):
		self.sueldo = s
	
	def obtener_sueldo(self):
		return self.sueldo
	
	def agregar_descuento_seguro(self,d_seguro):
		self.descuento = d_seguro
	
	def obtener_descuento_seguro(self):
		return self.descuento
#Calculamos el descuento final	
	def calculo_descuento_final(self):
		self.descuento_final = self.obtener_descuento_seguro() /100
		return self.descuento_final
#Calculamos el sueldo final	
	def obtener_sueldo_final(self):
		self.sueldo_final = self.obtener_sueldo()-(self.obtener_sueldo()*self.calculo_descuento_final())
		return self.sueldo_final
#Presentamos los datos de super y los datos de esta clase	
	def presentar_datos(self):
		cadena = "%s\nDescuento seguro: %f \nSueldo Final: %f\n" % (super(EmpleadoFijo,self).presentar_datos(),self.obtener_descuento_seguro(),self.obtener_sueldo_final())
		return cadena


class EmpleadoPorSemana(Empleado):
#declaramos super aparte de las variables globales de la clase	
	def __init__(self):
		super(EmpleadoPorSemana,self).__init__()
		self.numero_semanas = 0
		self.valor_semana = 0.0
		self.sueldo_final = 0.0
#Se crean los respectivos get y set de cada variable	
	def agregar_semanas(self,n_semanas):
		self.numero_semanas = n_semanas
	
	def obtener_semanas(self):
		return self.numero_semanas
	
	def agregar_valor_semanas(self,v_semanas):
		self.valor_semana = v_semanas
	
	def obtener_valor_semanas(self):
		return self.valor_semana
#Calculamos el sueldo final dependiendo de las semanas
	def obtener_sueldo_final(self):
		self.sueldo_final = self.obtener_semanas() * self.obtener_valor_semanas()
		return self.sueldo_final
#Presentamos los datos de super y los de las variables de esta clase 
	def presentar_datos(self):
		cadena = "%s\nNumero de semanas: %d\nValor semanas: %.2f\nSueldo Final: %.2f"%(super(EmpleadoPorSemana,self).presentar_datos(),self.obtener_semanas(),self.obtener_valor_semanas(),self.obtener_sueldo_final())
		return cadena

