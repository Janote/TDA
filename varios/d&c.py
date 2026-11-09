## Ejercicio 1 
def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    medio = len(arr) // 2 ## divide 
    mitad_izq = merge_sort(arr[:medio]) 
    mitad_der = merge_sort(arr[medio:]) 

    return merge(mitad_izq, mitad_der)

def merge(izq, der):
    mergeados = []
    i = j = 0

    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            mergeados.append(izq[i])
            i += 1
        else:
            mergeados.append(der[j])
            j += 1

    mergeados.extend(izq[i:])
    mergeados.extend(der[j:])

    return mergeados

# 1.
# La linea del divide es la 6
# Conquer 7 y 8 
# Combine la linea 10.
# 2.
# Se divide en 2 subproblemas. 
# 3.
# El tamano de los subproblemas es n/2 , siendo n el tamano del arreglo.
# 4.
# O(n)
# 5.
# T(n) = { O(1) si n = 1, Oex(n log(n))}
# 6.
# n ^ log 2 2 = n ^ 1 , y el costo de lo que no es recursivo es Oex n , ya q en el combine siempre recorres todo.

## Ejercicio 2 
def busqueda_binaria (arr,objetivo,izq =0,der = None):
    if der is None:
        der = len(arr) - 1 
    if izq > der :
     return False # Elemento no encontrado
    medio = ( izq + der ) // 2 # Divide
    if arr [ medio ] == objetivo :
     return medio
    elif arr [ medio ] > objetivo :
     return busqueda_binaria ( arr , objetivo , izq , medio - 1) #Conquer 
    else:
        return busqueda_binaria ( arr , objetivo , medio + 1, der ) #Conquer and no combine.
## A.     
## B. Se divide en 1 subproblema.
## C. El tamano de este subproblema es n / 2 
## D. No hay combine, O(1). a = 1 . b = 2 , log2 1 = 0  n^0 = 1 , f(n) = Oex(1). 
## E. T(n)=T(n/2)+\Theta(1)
## F. T(n) = \Theta log n 

# ## Ejercicio 3 
# Ejercicio 3 (Complexity quest) ⋆
# Calcule la complejidad de un algoritmo que utiliza T(n) pasos para una entrada de tamaño n, donde T cumple:
# 1) T(n) = T(n − 2) + 5
# Oex(n)
# 2) T(n) = T(n − 1) + n
# Oex(n^2)
# 3) T(n) = T(n − 1) + √n
#  n* sqrt(n) 
# 
# 4) T(n) = T(n − 1) + n^2
# n^3 
# 5) T(n) = 2T(n − 1)
# 2 ^ n 
# 6) T(n) = T(n/2) + n
# (n + n/2 + n/4 + .... ) * n = n log n 
# 7) T(n) = T(n/2) + √n
# T.M a = 1,  b = 2,  logb a = log2 1 = 0 -> n^log2 1 = 1 ,f(n) = sqrt n  ->Oex(sqrt(n))
# 8) T(n) = T(n/2) + n^2
# T.M a = 1 , b = 2 , log2 1 =  0 = n ^ 0 = 1 , f(n) = n^2 -> Oex(n^2)
# 9) T(n) = 2T(n − 4)
# 2^n
# 10) T(n) = 2T(n/2) + log n
# 2^n 
# 11) T(n) = 3T(n/4)
# T.M a = 3, b =4 log4 3 no te da un numero entero , pero se q domina la rec -> O(n^(log4 3 ))
# 12) T(n) = 3T(n/4) + n
# T.M log4 3 Oex(n)


## Ejercicio 4
# a = 2
# b = 2 
# f = O(n)
# log 2 2 = 1 


def masAlaIzquierda(arr):
    if len(arr) <= 1:
        return True
    mitad = len(arr) // 2 
    mit_der = masAlaIzquierda(arr[mitad:])
    mit_izq = masAlaIzquierda(arr[:mitad])
    return mit_izq and mit_der and mitadesEnOrden(arr[:mitad],arr[mitad:])

def mitadesEnOrden(arr1,arr2):
    suma1 = sum(arr1)
    suma2 = sum(arr2)
    return suma1 > suma2

        

## Ejercicio 5    
def indiceEspejo(arr,izq=0,der=None):
    if der is None:
        der = len(arr) - 1 
    if izq > der:
        return False
    mitad = (der + izq) // 2
    ancla = arr[mitad]
    if ancla == mitad:
        return True
    elif ancla > mitad:
        return indiceEspejo(arr,izq,mitad - 1) 
    else:
        return indiceEspejo(arr,mitad+1,der)



## Estos dos son ejercicios que le pedi a GPT para practicar algo
def primeraAparicion(arr, x, izq=0, der=None):
    if der is None:
        der = len(arr) - 1 
    if izq > der:
        return -1
    mitad = (der + izq) // 2 
    valor = arr[mitad]
    if x == valor:
        res_izq = primeraAparicion(arr,x,izq,mitad -1)
        if res_izq != -1:
            return res_izq
        else:
            return mitad
    elif x > valor:
        return primeraAparicion(arr,x,mitad + 1,der)
    else:
        ## caso en q x < arr]mitad 
        return primeraAparicion(arr,x,izq,mitad -1)
    
arr = [1, 2, 2, 2, 5, 8, 9]
x = 2

def ultimaAparicion(arr, x, izq=0, der=None):
    if der is None:
        der = len(arr) - 1 
    if izq > der:
        return -1
    mitad = (der + izq) // 2 
    valor = arr[mitad]
    if x == valor:
        res_der = ultimaAparicion(arr,x,mitad + 1,der)
        if res_der != -1:
            return res_der 
        else:
            return mitad
    elif x > valor:
        return ultimaAparicion(arr,x,mitad + 1,der)
    else:
        ## caso en q x < arr]mitad 
        return ultimaAparicion(arr,x,izq,mitad -1)    


## Ejercicio 6
def potLogaritmica(a,b):
    assert b >= 0
    if b == 0: return 1
    else:
        mitad = potLogaritmica(a,b // 2)
        if b % 2 == 0:
            return mitad * mitad
        else: # b es impar
            return a * mitad * mitad

## Ejercicio 7 - TODO

## Ejercicio 8:
# def cazadorDeFalsos(n):
#     return buscar(0, n - 1, 0, n - 1)

# def buscar(i0, i1, j0, j1):
#     if i0 == i1 and j0 == j1:
#         return (i0, j0)

#     if j0 < j1:                      # Primero dividimos columnas
#         medio = (j0 + j1) // 2

#         if not conjuncionSubmatriz(i0, i1, j0, medio):
#             return buscar(i0, i1, j0, medio)
#         else:
#             return buscar(i0, i1, medio + 1, j1)

#     else:                            # Queda una columna: dividimos filas
#         medio = (i0 + i1) // 2

#         if not conjuncionSubmatriz(i0, medio, j0, j1):
#             return buscar(i0, medio, j0, j1)
#         else:
#             return buscar(medio + 1, i1, j0, j1)
# ##



## Ejercico 9 
def maxSubsecuencia(arr):
    if len(arr) == 1: return arr[0]
    else:
        mitad = len(arr) // 2
        mit_izq = maxSubsecuencia(arr[:mitad])
        mit_der = maxSubsecuencia(arr[mitad:])
        cruzado = sumaCruzada(arr[:mitad],arr[mitad:])
        return max(mit_izq,cruzado,mit_der)

def sumaCruzada(s,t):
    res1 = mejorSumaPosible(s)
    res2 = mejorSumaPosiblev2(t)
    cruzar = res1 + res2
    return cruzar



def mejorSumaPosiblev2(t):
    maxValor = float('-inf')
    i = 0
    sum = 0
    while i < len(t)  :
        sum += t[i]
        maxValor = max(maxValor,sum)
        i += 1
    return maxValor

def mejorSumaPosible(s):
    maxValor = float('-inf')
    i = len(s) - 1
    sum = 0
    while i >= 0 :
        sum += s[i]
        maxValor = max(maxValor,sum)
        i -= 1
    return maxValor



## Ejercicio 10: Tengo una matriz de 4x4, supongamos:
# A = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]

def potMatriz(n):
    if n == 1: return A
    else:
        mitad = n // 2
        restante = potMatriz(mitad)
        actual = A.potencia(mitad)
        return restante + actual * (restante)
    

A = [1,2,3,4]
B = [6,4,2,1]

def difMinima(A,B,izq=0,der=None):
    if der is None:
        der = len(A) - 1 
    if izq > der:
        return float('inf')
    if izq == der: return abs(A[izq] - B[der])
    else:
        mitad = (izq + der) // 2
        mit_izq = difMinima(A,B,izq,mitad)
        mit_der = difMinima(A,B,mitad+1,der)
        return min(mit_izq,mit_der)

def contarCruzadas(arr1,arr2):
    count = 0
    i = 0   
    j = len(arr2) - 1 
    while i < len(arr1):
        while j >= 0:
            if arr1[i] > arr2[j]:
                count += j + 1 
                j = - 1
            else:
                j -= 1 
        j = len(arr2) - 1  
        i += 1 
    return count 
arreglito = [1, 3, 5, 2, 4]
def contarInversiones(arr, izq=0, der=None):
    if der is None:
        der = len(arr) - 1

    if izq >= der:
        return 0

    mitad = (izq + der) // 2

    mit_izq = contarInversiones(arr, izq, mitad)
    mit_der = contarInversiones(arr, mitad + 1, der)

    cruzadas = contarCruzadas(
        arr[izq:mitad + 1],
        sorted(arr[mitad + 1:der + 1])
    )

    return mit_izq + mit_der + cruzadas

B = [34, 1]

def ubicar(arr, objetivo, i=0, d=None):
    if d is None:
        d = len(arr) - 1

    mitad = (i + d) // 2

    if arr[mitad] == objetivo:
        return mitad

    if arr.aparece(i, mitad, objetivo):
        return ubicar(arr, objetivo, i, mitad)
    else:
        return ubicar(arr, objetivo, mitad + 1, d)


# Correctitud:
# El intervalo actual siempre contiene al elemento buscado. Si el elemento
# central es el objetivo, se devuelve su índice. En caso contrario, aparece
# permite determinar qué mitad contiene al objetivo. Se conserva esa mitad,
# que es estrictamente más pequeña cuando el intervalo tiene más de un elemento.
# Cuando queda un único elemento, necesariamente es el buscado y se devuelve
# su índice. No se requiere que el arreglo esté ordenado.

#  b) Complejidad temporal

# Para un intervalo de tamaño m:
# - Calcular el medio y comparar cuesta O(1).
# - Consultar aparece sobre la mitad cuesta O(sqrt(m)).
# - Se ejecuta UNA llamada recursiva sobre aproximadamente la mitad.
#   Las ramas if y else son excluyentes: a = 1, no a = 2.

# La recurrencia para una cota superior es:

#  T(n) <= T(ceil(n/2)) + O(sqrt(n)), con caso base O(1).

# Ignorando redondeos para simplificar la suma de costos por nivel:

#  T(n) = O(sqrt(n) + sqrt(n/2) + sqrt(n/4) + ...)
#       = O(sqrt(n) * (1 + 1/sqrt(2) + 1/2 + ...))
#       = O(sqrt(n)).

# La serie geométrica tiene razón 1/sqrt(2) < 1, por lo que su suma
# está acotada por una constante.

# También puede aplicarse el tercer caso del teorema maestro a una
# recurrencia que acote el costo, con a = 1, b = 2 y f(n) = sqrt(n):
# n^(log_b(a)) = 1; sqrt(n) es polinómicamente mayor y satisface regularidad,
# ya que sqrt(n/2) = sqrt(n)/sqrt(2).

# Resultado: O(sqrt(n)), que es sublineal porque sqrt(n)/n tiende a 0.

# No se afirma necesariamente Theta(sqrt(n)): el enunciado solo garantiza
# una cota O(sqrt(m)) para aparece, no un costo Theta(sqrt(m)).    