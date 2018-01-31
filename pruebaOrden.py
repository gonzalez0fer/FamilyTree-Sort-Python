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
# En este codigo se importan todos los algoritmos de ordenamiento solicitados          #
# para la evaluacion de efectividad de los mismos para ordenar arreglos de             #
# Strings, este lanzador permitira la opcion de hacer la prueba de los algoritmos      #
# directamente a partir de una lista de N-elementos, o bien desde una lista            #
# en PreOrden generada a partir de un arbol de N-elementos, por otra parte tambien     #
# permitira a elegivilidad del numero de corridas a promediar, asi como tambien del    #
# numero de elementos de la misma y los algoritmos a usar (Nlgn o All).                #
# Para ejecutarlo por terminar debe introducir:                                        #
#                                                                                      #
# python pruebaOrden.py <arbol|lista> <all|nlgn> <numeroDePruebas> <numeroDeElementos> #
#                                                                                      #
# Donde los primeros 2 argumentos son opciones de tipo de corrida:                     #
# ejemplo:                                                                             #
#                                                                                      #
# python pruebaOrden.py arbol nlgn 5 1000                                              #
#                                                                                      #
# >>>>>> creara un arbol de 1000 elementos y a partir de el generera una lista en      #
# preOrden con todos esos elementos y la sometera a 5 corridas de cada algoritmo de    #
# ordenamiento  (en este caso solo los Nlgn)e imprimira en terminal el promedio        #
# de tiempo en que tardo cada algoritmo en ordenar a los mil nombres de caracteres     #
# aleatorios de cardinalidad 7....                                                     #
########################################################################################

import sys,random, time, string
from ordenamiento import *
from Nodo import *

########################################################################################
# Esta funcion recibe un entero n y retorna una lista con n palabras de largo 7 para
# luego ser ordenada por los algoritmos deseados
def obtenerArreglo(n):
    lista = []
    for i in range(0,n):
        a = ''.join(random.choice(string.ascii_uppercase) for _ in range(7))
        lista.append(a)
    return lista
########################################################################################
# Esta funcion recibe un entero n con el cual crea un arbol de n palabras de largo 7
# en sus nodos para luego generar una lista en Preorder con todos sus nombres para luego
# ser ordenada por los algoritmos deseados
def GeneradorArbol(n):

    _Arbol = Nodo()
    lista = []
    for i in range(0,n):

        a = ''.join(random.choice(string.ascii_uppercase) for _ in range(7))
        lista.append(a)

    for i in range(0,len(lista)):
        l = lista[i]
        _Arbol.insertar(l)

    _Arbol.Preorden(_Arbol.elem)

    return(_Arbol.lista_())

########################################################################################
# esta funcion recibe los argumentos a partir del terminal e imprime un mensaje si
# no se coloca el numero de argumentos necesario
def parseArgs(args):
    msg = "Error en la linea de comando:\npruebaOrdenamiento.py [Arbol|Lista] [all|nlgn] <numero de pruebas> <numero de elementos>"
    if len(args) != 5:
        print(msg)
        sys.exit(1)

    if (args[1] != 'arbol' and args[1] != 'lista'):
        print(msg)
        sys.exit(1)

    if (args[2] != "all" and args[2] != "nlgn"):
        print(msg)
        sys.exit(2)

    return args[1], args[2], int(args[3]), int(args[4])


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

###########################################################################
#  funcion que recibe las listas y las pasa por los diversos algoritmos de
# ordenamiento elegidos en un unicio, retornando los tiempos de corrida de
# cada uno de ellos
def probarAlgoritmos(datos,tipo):

    if tipo == "all" :
        print("Comenzando InsertionSort")
        start_time = time.time()
        arrayResult = list(datos)
        insertionsort(arrayResult)
        assert(estaOrdenado(arrayResult))
        timeIsertion = time.time() - start_time

        print("Comenzando Bubblesort")
        start_time = time.time()
        arrayResult = list(datos)
        bubblesort(arrayResult)
        assert(estaOrdenado(arrayResult))
        timeBubblesort1 = time.time() - start_time

        time_N_2 = (("Insertionsort", timeIsertion),("Bubblesort", timeBubblesort1))
    else :
        time_N_2 = ()

    print("Comenzando Quicksort")
    start_time = time.time()
    arrayResult = list(datos)
    quicksort(arrayResult)
    assert(estaOrdenado(arrayResult))
    timeQuicksort = time.time() - start_time
    
    print("Comenzando mergesort")
    start_time = time.time()
    arrayResult = list(datos)
    mergesort(arrayResult)
    assert(estaOrdenado(arrayResult))
    timeMergesort = time.time() - start_time
    
    print("Comenzando heapsort")
    start_time = time.time()
    arrayResult = list(datos)
    heapsort(arrayResult)
    assert(estaOrdenado(arrayResult))
    timeHeapsort = time.time() - start_time

    time_N_lg_N = (("Quicksort", timeQuicksort), ("Mergesort", timeMergesort), ("Heapsort", timeHeapsort))

    return time_N_lg_N + time_N_2

##################################################################################
# Funcion que recibe el numero de pruebas y de elementos a realizas ademas del
# tipo de algoritmos a utilizas (todos o solo los nlgn) ademas de si la lista a
# ordenar se genera desde un arbol o se genera de manera directa. y los resultados
# los coloca en una lista.
def realizarPruebas(numPruebas, numElems, tipo,tipo2):
    datos = []
    resultadosPruebas = []
    for i in range(numPruebas) :
        print("\nComenzando la prueba: "+str(i+1))
        if tipo2 == 'lista':
            datos = obtenerArreglo(numElems)
        elif tipo2 == 'arbol':
            datos = GeneradorArbol(numElems)
        else:
            pass

        r = probarAlgoritmos(datos, tipoDeCorrida)
        resultadosPruebas.append(r)
    return resultadosPruebas



################################################################################
# Esta funcion recibe la lista de resultados y promedia los resultados de las
# corridas, imprimiendo en terminal un valor float de dos decimales indicando
# el tiempo de corrida de cada algoritmo por separado.
def procesarResultados(results):
    print("")
    
#---------------------------Promedios-------------------------------------------
    sum_Quick = 0
    sum_Merge = 0
    sum_Heap = 0
    sum_Inser = 0
    sum_Burb1 = 0
    
    cont_Quick = 0
    cont_Merge = 0
    cont_Heap = 0
    cont_Inser = 0
    cont_Burb1 = 0
    
    for i in range(len(results)):
        for j in range(len(results[i])):
            if results[i][j][0] == 'Quicksort':
                sum_Quick = sum_Quick + float(results[i][j][1])
                cont_Quick = cont_Quick + 1
                
            elif results[i][j][0] == 'Mergesort':
                sum_Merge = sum_Merge + float(results[i][j][1])
                cont_Merge = cont_Merge + 1
                
            elif results[i][j][0] == 'Heapsort':
                sum_Heap = sum_Heap + float(results[i][j][1])
                cont_Heap = cont_Heap + 1
                
            elif results[i][j][0] == 'Insertionsort':
                sum_Inser = sum_Inser + float(results[i][j][1])
                cont_Inser = cont_Inser + 1
                
            elif results[i][j][0] == 'Bubblesort':
                sum_Burb1 = sum_Burb1 + float(results[i][j][1])
                cont_Burb1 = cont_Burb1 + 1
                
    promedio_Quick = sum_Quick / cont_Quick
    promedio_Merge = sum_Merge / cont_Merge
    promedio_Heap = sum_Heap / cont_Heap
    
    if (cont_Inser != 0) and (cont_Burb1 != 0):
        promedio_Inser = sum_Inser / cont_Inser
        promedio_Burb1 = sum_Burb1 / cont_Burb1
    

    print('Quicksort' + ' ' + "%.2f" % (promedio_Quick*(10**3))) 
    print('Mergesort' + ' ' + "%.2f" % (promedio_Merge*(10**3)))
    print('Heapsort' + ' ' + "%.2f" % (promedio_Heap*(10**3))) 
    
    if (cont_Inser != 0) and (cont_Burb1 != 0):
        print('Insertionsort' + ' ' + "%.2f" % (promedio_Inser*(10**3))) 
        print('Bubblesort' + ' ' + "%.2f" % (promedio_Burb1*(10**3)))
 

########################################################################################
#                                                                                      #
######                              MAIN PROGRAM                                  ######
#                                                                                      #
########################################################################################                  

if __name__ == "__main__":
    tipoDeGenerador,tipoDeCorrida, numPruebas, numElems = parseArgs(sys.argv)
    results = realizarPruebas(numPruebas, numElems, tipoDeCorrida, tipoDeGenerador)
    procesarResultados(results)