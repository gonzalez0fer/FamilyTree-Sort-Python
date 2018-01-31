#########################################################################################
#																					    #
#         # JOSE ####																    #
#       ### \/#|### |/####																#
#      ##\/#/ \||/JAN/_/##/_#															#
#    ###  \/JUAN|/ \/ # PEPE      ______                _ __     ______             	#
#  ##_\_#\_\## | #/###_/_####    / ____/___ _____ ___  (_) /_  _/_  __/_______  ___ 	#
# ## MARY # \ #| /  LILI ##/##  / /_  / __ `/ __ `__ \/ / / / / // / / ___/ _ \/ _ \	#
#  __#_--###`  |{,###---###-~  / __/ / /_/ / / / / / / / / /_/ // / / /  /  __/  __/	#
#            \ }{             /_/    \__,_/_/ /_/ /_/_/_/\__, //_/ /_/   \___/\___/ 	#
#             }}{                                       /____/							#
#             }}{																		#
#             {{}					Integrantes: Fernando Gonzalez 08-10464	         	#
#       , -=-~{ .-^- _____ 						 Bruno Colmenares 12-10551				#
#             `}					     Laboratorio Algoritmos II grupo 9   			#
#              {																		#
#########################################################################################

########################################################################################
################################      README      ######################################
########################################################################################
# En este codigo se encuentra la estructura de arbol junto con todas las funciones     #
# pertinentes para la elaboracion del proyecto, esta estructura posee cabecera, es     #
# decir, tiene una clase Hoja la cual se utiliza para definir los parametros de cada   #
# uno de los elementos que estan relacionados entre si bajo la estructura de un        #
# arbol binario. estas funciones seran utilizadas a conveniencia en el archivo de      #
# familyTree.py para la creacion de un arbol genealogico y su posterior modificacion   #
# e impresion en un archivo de salida relacionando cada elemento por medio de la       #
# relacion Padre: hijoIzquierdo hijoDerecho, acada uno acompaniado de un numero asig-  #
# nado durante la construccion, ademas de las salidas en inOrden, preOrden y posOrden  #
########################################################################################


class Hoja:
##############################################################################
# clase en la cual se crea un objeto Hoja (nodo), el cual pasara a contener toda
# la informacion pertinente a la construccion del arbol.
	def __init__ (self, nombre = None, numero = None, padre = None, hojaizq=None, hojader=None):
		self.nombre = nombre
		self.numero = numero
		self.padre = padre
		self.hojaizq = hojaizq
		self.hojader = hojader

##############################################################################
# Esta funcion es urilizada para la modificacion del arbol y funciona para
# agregar un nuevo nodo por la izquierda un determinado nodo que reciba 
	def add_hojaizq(self, nombre, numero, padre=None, hojaizq=None, hojader=None):
		actual = self
		if actual.hojaizq == None:
			actual.hojaizq = Hoja(nombre, numero, padre, hojaizq, hojader)
			return(actual.hojaizq)
		else:
			pass

##############################################################################
# Esta funcion es urilizada para la modificacion del arbol y funciona para
# agregar un nuevo nodo por la derecha un determinado nodo que reciba 
	def add_hojader(self, nombre, numero, padre=None, hojaizq=None, hojader=None):
		actual = self
		if actual.hojader == None:
			actual.hojader = Hoja(nombre, numero, padre, hojaizq, hojader)
			return (actual.hojader)
		else:
			pass
##############################################################################
# Esta funcion retorna un booleano si un determinado nodo tiene hijo izquierdo o no 
	def tiene_hojaizq(self):
		aux = self
		if aux.hojaizq == None:
			return False
		else:
			return True
##############################################################################
# Esta funcion retorna un booleano si un determinado nodo tiene hijo derecho o no 
	def tiene_hojader(self):
		aux = self
		if aux.hojader == None:
			return False
		else:
			return True
##############################################################################
# Esta funcion retorna un booleano si un determinado nodo tiene hijos o no 
	def tiene_hijos(self):
		if self.tiene_hojader() or self.tiene_hojaizq():
			return True
		else:
			return False




class Arbol:
##############################################################################
# clase en la cual se inicializa una raiz vacia para un arbol binario
	def __init__ (self):
		self.raiz = None

##############################################################################
# Esta funcion recibe tres diccionarios que almacenan la informacion que relaciona
# a los nodos a ser agregados en el arbol en un determinado nodo que recibe. con esta
# informacion contenida en los diccionarios procede a agregar recursivamente desde la
# raiz todos y cada uno de los hijos izquierdos y derechos, respetando las relaciones
# como el orden dentro de la estructura de arbol binario
	def crear(self, dicc1, dicc2, dicc3, nombre, nodo, padre = None):
		DicNumero = dicc1
		DicHijoIzq = dicc2
		DicHijoDer = dicc3
		if self.arbol_esVacio():
			self.raiz = nodo
			self.raiz.nombre = nombre
			self.raiz.numero = DicNumero[nombre]
			self.raiz.padre = padre
		else:
			nodo.nombre = nombre
			nodo.numero = DicNumero[nombre]
			nodo.padre = padre
		if nodo.nombre in DicHijoIzq:
			nodo.hojaizq = Hoja()
			self.crear(DicNumero, DicHijoIzq, DicHijoDer, DicHijoIzq[nodo.nombre], nodo.hojaizq, nodo)
		if nodo.nombre in DicHijoDer:
			nodo.hojader = Hoja()
			self.crear(DicNumero,DicHijoIzq,DicHijoDer, DicHijoDer[nodo.nombre], nodo.hojader, nodo)


##############################################################################
# Esta funcion recibe un nodo a partir del cual va a buscar el dato 'nombre' 
# solicitado dentro de cada nodo del arbol, al encontrarlo regresa el nodo
# cuyo dato asociado es el nombre proporcionado. se utiliza para la modificacion
# del arbol en el archivo familyTree.py
	def buscar_hoja(self, nodo, nombre):

		if nodo is not None:
			aux = nodo
			if aux.nombre == nombre:
				return aux
			if aux.tiene_hojaizq():
				n = self.buscar_hoja(nodo.hojaizq, nombre)
				if n ==None:
					return self.buscar_hoja(nodo.hojader, nombre)
				else:
					return n
			elif aux.tiene_hojader():
				return self.buscar_hoja(nodo.hojader, nombre)
			else:
				return None

##############################################################################
# Funcion que retorna un booleano si el arbol tiene o no tiene elementos
	def arbol_esVacio(self):
		if self.raiz == None:
			return True
		else:
			return False

##############################################################################
# Funcion que imprime todos y cada uno de los elementos del arbol en preOrden
# en el archivo de salida
	def pre_order(self, nodo, archivo_salida):
		arch = open(archivo_salida,'a')
		if nodo is not None:
			arch.write(nodo.nombre+ ' ')
			arch.close()
			self.pre_order(nodo.hojaizq, archivo_salida)
			self.pre_order(nodo.hojader, archivo_salida)
		else:
			return


##############################################################################
# Funcion que imprime todos y cada uno de los elementos del arbol en inOrden
# en el archivo de salida
	def in_order(self, nodo,archivo_salida):
		arch = open(archivo_salida,'a')
		if nodo is not None:
			self.in_order(nodo.hojaizq,archivo_salida)
			arch.write(nodo.nombre + ' ')
			arch.close()
			self.in_order(nodo.hojader,archivo_salida)
		else:
			return	

##############################################################################
# Funcion que imprime todos y cada uno de los elementos del arbol en posOrden
# en el archivo de salida
	def post_order(self, nodo, archivo_salida):
		arch = open(archivo_salida,'a')
		if nodo is not None:
			if nodo.hojaizq:
				self.post_order(nodo.hojaizq,archivo_salida)
			if nodo.hojader:
				self.post_order(nodo.hojader,archivo_salida)
			arch.write(nodo.nombre + ' ')			
			arch.close()
		else:
			return

##############################################################################
# Funcion que imprime en el archivo de salida todas las relaciones de tipo
# 'Padre: hijos' acompaniados del numero asignado a cada uno de ellos
# ejm. Padre (#): HijoIzq (#) HijoDer (#)
	def mostrar_ramas(self, nodo, archivo_salida):
		arch = open(archivo_salida,'a')
		if (nodo and nodo.hojaizq and nodo.hojader) is not None:
			arch.write(str(nodo.nombre)+' (' +str(nodo.numero)+'): '+str(nodo.hojaizq.nombre)+\
				' ('+str(nodo.hojaizq.numero) +') '+ str(nodo.hojader.nombre) +' ('+ str(nodo.hojader.numero)+')'+'\n')
			arch.close()
		elif (nodo and nodo.hojaizq) is not None:
			arch.write(str(nodo.nombre)+' ('+str(nodo.numero)+'): '+str(nodo.hojaizq.nombre)+\
				' ('+str(nodo.hojaizq.numero)+')'+'\n')
			arch.close()
		elif (nodo and nodo.hojader) is not None:
			arch.write(str(nodo.nombre)+' ('+str(nodo.numero) +'): '+str(nodo.hojader.nombre)+\
				' ('+str(nodo.hojader.numero)+')'+'\n')
			arch.close()
		elif nodo is not None:
			arch.write(str(nodo.nombre)+' ('+str(nodo.numero)+')'+'\n')
			arch.close()

		if nodo.hojaizq and nodo.hojaizq.tiene_hijos():	
			self.mostrar_ramas(nodo.hojaizq, archivo_salida)
		if nodo.hojader and nodo.hojader.tiene_hijos():
			self.mostrar_ramas(nodo.hojader, archivo_salida)
