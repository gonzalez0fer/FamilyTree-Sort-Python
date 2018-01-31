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
# En este codigo se encuentran todos los algoritmos de ordenamiento solicitados a ser  #
# importados por el archivo pruebaOrden.py para la evaluacion de la efectividad en     #
# tiempo de cada uno de ellos, estos algoritmos son codigos ya establecidos en         #
# diferentes fuentes bibliograficas referentes al tema.                                #
########################################################################################


import random

##############################################################################
# algoritmo de ordenamiento por burbuja
def bubblesort(lista):
    length = len(lista) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if lista[i] > lista[i+1]:
                sorted = False
                lista[i], lista[i+1] = lista[i+1], lista[i]

##############################################################################
# algoritmo de ordenamiento por insercion
def insertionsort(lista):
    """ Implementation of insertion sort """
    for i in range(1, len(lista)):
        j = i
        while j > 0 and lista[j] < lista[j-1]:
            lista[j], lista[j-1] = lista[j-1], lista[j]
            j -= 1

##############################################################################
# algoritmo de ordenamiento rapido

def quicksort( lista ):
    _quicksort( lista, 0, len( lista ) - 1 )
 
def _quicksort( lista, primero, ultimo ):
    if primero < ultimo:
      pivote = partition( lista, primero, ultimo )
      _quicksort( lista, primero, pivote - 1 )
      _quicksort( lista, pivote + 1, ultimo )
 
 
def partition( lista, primero, ultimo ) :
    pivote = primero + random.randrange( ultimo - primero + 1 )
    swap( lista, pivote, ultimo )
    for i in range( primero, ultimo ):
      if lista[i] <= lista[ultimo]:
        swap( lista, i, primero )
        primero += 1
 
    swap( lista, primero, ultimo )
    return primero


###################################################################
# algoritmo de ordenamiento por montículos (heapsort, en ingles)
def heapsort( lista ):

    length = len( lista ) - 1
    leastParent = length // 2
    for i in range ( leastParent, -1, -1 ):
      moveDown( lista, i, length )
 

    for i in range ( length, 0, -1 ):
      if lista[0] > lista[i]:
        swap( lista, 0, i )
        moveDown( lista, 0, i - 1 )
 
 
def moveDown( lista, primero, ultimo ):
    largest = 2 * primero + 1
    while largest <= ultimo:

      if ( largest < ultimo ) and ( lista[largest] < lista[largest + 1] ):
        largest += 1
 
      if lista[largest] > lista[primero]:
        swap( lista, largest, primero )

        primero = largest;
        largest = 2 * primero + 1
      else:
        return 



def swap( A, x, y ):
  temporal = A[x]
  A[x] = A[y]
  A[y] = temporal


#######################################################################
# Algoritmo de ordenamiento por mezcla

def mergesort( lista ):
  _mergesort( lista, 0, len( lista ) - 1 )
 
 
def _mergesort( lista, primero, ultimo ):

  mitad = ( primero + ultimo ) // 2
  if primero < ultimo:
    _mergesort( lista, primero, mitad )
    _mergesort( lista, mitad + 1, ultimo )
 
  a, f, l = 0, primero, mitad + 1
  temporal = [None] * ( ultimo - primero + 1 )
 
  while f <= mitad and l <= ultimo:
    if lista[f] < lista[l] :
      temporal[a] = lista[f]
      f += 1
    else:
      temporal[a] = lista[l]
      l += 1
    a += 1
 
  if f <= mitad :
    temporal[a:] = lista[f:mitad + 1]
 
  if l <= ultimo:
    temporal[a:] = lista[l:ultimo + 1]
 
  a = 0
  while primero <= ultimo:
    lista[primero] = temporal[a]
    primero += 1
    a += 1


###############################################################################
# Funcion que retorna un booleano si la lista  que recibe esta o no ordenada.
def estaOrdenado(a):
    ordenado = True
    i = 1
    while (i < len(a)) and ordenado:
        if a[i-1] <= a[i]:
            pass
            
        elif a[i-1] > a[i]:
            ordenado = False
            
        i = i + 1
    return ordenado

