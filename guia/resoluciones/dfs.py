from collections import deque
visitados = [False] * 6 
aristas = [[2],[3],[4],[],[4],[3]]

def dfs(v):
    visitados[v] = True
    for elem in aristas[v]:
        if (not(visitados[elem])):
            ## Si no esta visitado, lo visito.
            dfs(elem)



def conexidadAPartirDeV(v):
    dfs(v);
    for i in range(len(visitados)):
        if visitados[i] != True:
            return False
    return True


def contarComponentesConexas():
    componentes = 0
    for i in range(len(visitados)):
        if not(visitados[i]):
            componentes += 1
            conexidadAPartirDeV(i)
    return componentes


print(contarComponentesConexas())


def esquemaPiramidal():