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
# En este codigo se encuentran las diversas llamadas para la construccion y modifi -   #
# cacion del arbol generacional de los nombres tomados a partir de los archivos de     #
# entrada. el codigo recibe dos archivos de entrada, el primero contiene una serie de  #
# nombres conexos bajo la relacion de 'A es padre de B' en un orden aleatorio, por     #
# lo cual el codigo se encarga de ordenar y construir el arbol a partir de esas lineas.#
# en el segundo archivo, se encuentran una serie de correcciones del arbol inicialmente#
# planteado, y el codigo se encarga de interpretar dichos errores y mover las ramas y\o#
# hojas relativas a la correccion para finalmente imprimir un archivo de salida con la #
# estructura corregida y el arbol en inOrden, PreOrden y PostOrden                     #
########################################################################################

from arbol import * 
import sys, os

class familyTree:

##############################################################################
# clase en la cual se crea un arbol vacio a partir de la estructura de arbol
# guardada en el archivo arbol.py
	def __init__ (self, contador = 0):
		self.arbol_gen = Arbol()

##############################################################################
# Para la construccion del arbol, el codigo del arbol se vale de 3 diccionarios
# en los cuales se almacena una clave por cada elemento que cumple una deter-
# minada condicion. en el primer diccionario se almacenan los numeros referentes
# al orden en el que son leidos todos los elementos del archivo_entrada1 
# teniendo como clave el elemento en si y como valor asociado el numero. en
# el segundo y tercer diccionario se almacenan como valores los hijos izquierdo
# y derecho respectivamente asociados al padre en la clave (si los tiene).
# determina el padre por medio de una lista que guarda a todos los elementos
# siendo la raiz del arbol, aquel que no tiene padre, es decir que no se 
# encuentre como valor en ninguno de los diccionarios de hjios.
# a partir de alli agrega recursivamente todos los elementos del arbol de manera
# doblemente enlazada con el padre de cada cual.
	def construir_arbol(self, archivo_entrada1):

		arch = open(archivo_entrada1,'r')
		linea = arch.readline()
		lista = linea.split()
		cont = 0
		DicNumero = {}
		DicHijoDer = {}
		DicHijoIzq = {}
		auxiliar = []
	#############################################
	# Construccion de los 3 diccionarios
	# en DicNumero almacena todos los nombres junto
	# con el numero en el que fue leido
	# en DicHijoIzq almacena a todos los nombres
	# que tienen hijos izquierdo, con el hijo en el valor asociado
	# en DiccHijoDer se guardan todos los que tienen
	# hijo derecho, con el hijo en el valor asociado
		while (linea !=""):

			if lista != []:

				if len(lista) == 3:
					if lista[0] not in DicNumero:
						DicNumero[lista[0]] = cont
						if lista[0] not in auxiliar:
							auxiliar.append(lista[0])
						else:
							pass	
						cont+=1
					else:
						pass

					if lista[1] not in DicNumero:						
						DicNumero[lista[1]] = cont
						if lista[1] not in auxiliar:
							auxiliar.append(lista[1])
						else:
							pass
						cont += 1
					else:
						pass
					if lista[2] not in DicNumero:						
						DicNumero[lista[2]] = cont
						if lista[2] not in auxiliar:
							auxiliar.append(lista[2])
						else:
							pass
						cont += 1
					else:
						pass
					DicHijoDer[lista[0]] = lista[2]
					DicHijoIzq[lista[0]] = lista[1]
				else:
					pass



				if len(lista) == 2:
					if lista[0] not in DicNumero:
						DicNumero[lista[0]] = cont
						if lista[0] not in auxiliar:
							auxiliar.append(lista[0])
						else:
							pass
						cont+=1
					else:
						pass
					if lista[1] not in DicNumero:						
						DicNumero[lista[1]] = cont
						if lista[1] not in auxiliar:
							auxiliar.append(lista[1])
						else:
							pass
						cont += 1
					else:
						pass

					if lista[0] in DicHijoIzq:
						DicHijoDer[lista[0]] = lista[1]
					else:
						DicHijoIzq[lista[0]] = lista[1]
				else:
					pass


				if len(lista) == 1:
					if lista[0] not in DicNumero:
						DicNumero[lista[0]] = cont
						if lista[0] not in auxiliar:
							auxiliar.append(lista[0])
						else:
							pass	
						cont+=1
					else:
						pass
			else:
				pass
			linea = arch.readline()
			lista = linea.split()

	#############################################
	# Determinando cual es la raiz del arbol
		for i in range (0, len(auxiliar)):
			if auxiliar[i] not in DicHijoIzq.values() and auxiliar[i] not in DicHijoDer.values():
				padre = auxiliar[i]
			else:
				pass
	#############################################
	# se llama a la funcion que agrega de forma 
	# recursiva a  todos los elementos del arbol
		nodo_apoyo = Hoja()
		self.arbol_gen.crear(DicNumero, DicHijoIzq, DicHijoDer, padre, nodo_apoyo)

##############################################################################
# Para la modificacion del arbol se lee un segundo archivo de entrada en el
# cual se encuentran las correcciones a aplicar al arbol. en esta funcion se
# busca el nodo al cual se quiere aplicar la modificacion, y se comprueba que
# el error existe, si existe copia la informacion del nodo y busca al nuevo padre
# para luego enlazarlo con el nodo copiado y finalmente corta el nodo del antiguo
# padre 
	def corregir_arbol(self, archivo_entrada2):

		arch = open(archivo_entrada2,'r')
		linea = arch.readline()
		listado = linea.split()

		while (linea !=""):


			if listado != []:
			#############################################
			# Busca el nodo a modificar
				aux2 = self.arbol_gen.buscar_hoja(self.arbol_gen.raiz, listado[1])
			#############################################
			# Comprueba si esta correcta la modificacion
				if aux2.padre.nombre == listado[0]:
					pass
				else:
				#############################################
				# Busca guarda la informacion del nodo y busca 
				# al nuevo padre y al padre erroneo, asigna
				# al nuevo y corta el enlace con el padre erroneo
					antiguo_padre = aux2.padre.nombre
					nuevo_padre = self.arbol_gen.buscar_hoja(self.arbol_gen.raiz, listado[0])
					rama = aux2
					viejo_padre = self.arbol_gen.buscar_hoja(self.arbol_gen.raiz, antiguo_padre)					
					if viejo_padre.hojaizq.nombre == listado[1]:
						viejo_padre.hojaizq = None
					elif viejo_padre.hojader.nombre == listado[1]:
						viejo_padre.hojader = None
					if nuevo_padre.tiene_hojaizq():
						nuevo_padre.add_hojader (rama.nombre, rama.numero, nuevo_padre, rama.hojaizq, rama.hojader)
					else:
						h= nuevo_padre.add_hojaizq (rama.nombre, rama.numero, nuevo_padre, rama.hojaizq, rama.hojader)


			linea = arch.readline()
			listado = linea.split()

##############################################################################
# Esta funcion hace el llamado de la funcion que imprime en el archivo de salida
# el arbol ya modificado en donde selen las relaciones Padre e hijos junto con
# los numeros asignados a cada uno
	def mostrarArbol_gen(self, archivo_salida):
		self.arbol_gen.mostrar_ramas(self.arbol_gen.raiz, archivo_salida)


##############################################################################
# Esta funcion hace el llamado de la funcion que imprime en el archivo de salida
# el arreglo de los numeros en PreOrden


	def pre_order(self, archivo_salida):
		self.arbol_gen.pre_order(self.arbol_gen.raiz, archivo_salida)


##############################################################################
# Esta funcion hace el llamado de la funcion que imprime en el archivo de salida
# el arreglo de los numeros en InOrden
	def in_order(self,archivo_salida):
		self.arbol_gen.in_order(self.arbol_gen.raiz, archivo_salida)


##############################################################################
# Esta funcion hace el llamado de la funcion que imprime en el archivo de salida
# el arreglo de los numeros en PostOrden
	def post_order(self,archivo_salida):
		self.arbol_gen.post_order(self.arbol_gen.raiz, archivo_salida)


##############################################################################
# Esta funcion hace la funcion de NewLine en la impresion del archivo de
# salida
	def blankline(self, archivo_salida):
		arch = open(archivo_salida,'a')
		arch.write('\n')
		arch.close()


###############################################################################

########################################################################################
# esta funcion recibe los argumentos a partir del terminal e imprime un mensaje si
# no se coloca el numero de argumentos necesario o si son incorrectos
def parseArgs(args):
    msg = "Error en la linea de comando:\nfamilyTree.py <archivo_entrada1> <archivo_entrada2> <archivo_salida>"
    if len(args) != 4:
        print(msg)
        sys.exit(1)

    return args[1], args[2], args[3]



########################################################################################
#                                                                                      #
######                              MAIN PROGRAM                                  ######
#                                                                                      #
######################################################################################## 

if __name__ == "__main__":
    archivo_entrada1, archivo_entrada2, archivo_salida = parseArgs(sys.argv)
    if os.path.exists(archivo_salida):
        os.remove(archivo_salida)
    Arbol_familiar = familyTree()
    Arbol_familiar.construir_arbol(archivo_entrada1)
    Arbol_familiar.corregir_arbol(archivo_entrada2)
    Arbol_familiar.mostrarArbol_gen(archivo_salida)
    Arbol_familiar.blankline(archivo_salida)
    Arbol_familiar.pre_order(archivo_salida)
    Arbol_familiar.blankline(archivo_salida)
    Arbol_familiar.in_order(archivo_salida)
    Arbol_familiar.blankline(archivo_salida)
    Arbol_familiar.post_order(archivo_salida) 