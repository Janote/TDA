C = [4, 3, 7]
k = 10 

def sumaSubconjuntos(i,j):
    ## i representa la cantidad, j el k 
    if i < 0: 
        return j == 0
    
    elif j - C[i] < 0:
        return sumaSubconjuntos(i-1,j)
    else:
        return sumaSubconjuntos(i-1,j) or sumaSubconjuntos(i-1,j - C[i])

print(sumaSubconjuntos(len(C) - 1, k))

## Complejidad peor caso siempre cae en el else:
#                                   f(|C|,k)
#                                  /        \
#                                f(|C| - 1,k) f(|C| - 1,k - C[i])
# La altura del arbol seguro para el peor caso es |C|, q seria n, en un buen caso encuentra el k = 0 antes, pero se q me dijeron
# q en pd/ backtracking / d&C la complejidad es cantidad de estados * costo de trabajo, y se q aca tenese n * k estados distintos 
