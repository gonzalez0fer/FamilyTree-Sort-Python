#######################################################################################
##                                                                                   ##
##    ad88888ba                            888888888888                              ##
##   d8"     "8b                          ,d    88                        ,d         ##
##   Y8,                                  88    88                        88         ##
##   `Y8aaaaa,    ,adPPYba,  8b,dPPYba, MM88MMM 88  ,adPPYba, ,adPPYba, MM88MMM      ##
##     `"""""8b, a8"     "8a 88P'   "Y8   88    88 a8P_____88 I8[    ""   88         ##
##           `8b 8b       d8 88           88    88 8PP"""""""  `"Y8ba,    88         ##
##   Y8a     a8P "8a,   ,a8" 88           88,   88 "8b,   ,aa aa    ]8I   88,        ##
##    "Y88888P"   `"YbbdP"'  88           "Y888 88  `"Ybbd8"' `"YbbdP"'   "Y888      ##
##                                                                                   ##
##   Integrantes: Fernando Gonzalez 08-10464                                         ##
##                Bruno Colmenares 12- 10551                                         ##
##             Laboratorio Algoritmos II grupo 9                                     ##
##                                                                                   ##
#######################################################################################

########################################################################################
#############################      README      #########################################
########################################################################################
# En este codigo se encuentra la estructura de arbol sin cabecera vista en clases con  #
# la funcion insertar y la funcion de Preorden modificada para generar una lista de n  #
# elementos, en lugar de imprimirla esto para efectos de generar la lista para la      #
# prueba de los algoritmos de ordenamiento a partir de un arbol binario de busqueda    #
# con n-nombres de caracteres aleatorios de cardinalidad 7                             #
########################################################################################


class Nodo:

##############################################################################
# clase con los atributos para la creacion del nodo del arbol binario mas
# un atributo que almacenara una lista con todos los elementos del arbol
	def __init__(self, valor=None, padre=None, elem = []):
		self.izquierdo = None
		self.derecho = None
		self.valor = valor
		self.padre = padre
		self.elem = []
		
##############################################################################
# funcion que inserta cada nombre en orden alfabetico con relacion al padre
# de izquierda a derecha en un arbol binario de busqueda
	def insertar(self,valor):
		if self.valor == None:
			self.valor =valor
			return
		if valor<= self.valor:
			if self.izquierdo:
				self.izquierdo.insertar(valor)
			else:
				self.izquierdo = Nodo(valor, self)
		else:
			if self.derecho:
				self.derecho.insertar(valor)
			else:
				self.derecho = Nodo(valor, self)

##############################################################################
# funcion que inserta en una lista todos los elementos del arbol en preorden		
	def Preorden(self, lista):
		if self.valor:

			lista.append(self.valor)
			if self.izquierdo:
				self.izquierdo.Preorden(lista)
			if self.derecho:
				self.derecho.Preorden(lista)

		else:
			return
##############################################################################
# funcion que retorna la lista en preorden de todos los elementos del arbol
# dicha lista esta alojada en el constructor de la clase
	def lista_(self):
		return self.elem





