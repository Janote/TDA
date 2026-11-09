D = [2,1,3,2]


def deadlines():
    ## paso el arreglo a tuplas con indice antes de ordenar
    for i in range(len(D)):
        D[i] = (D[i],i+1)
    # Piola, ordeno pro la primer componentes
    D.sort()
    deadline_actual = -1
    deadlines = [] 

    for elem in D:
        if deadline_actual < elem[0]:
            deadlines.append(elem[1])
            deadline_actual = elem[0]
    
    return deadlines

print(deadlines())