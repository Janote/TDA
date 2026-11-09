n = int(input())
grafo = []
largo = 0

for _ in range(n):
    p = int(input())

    if p == -1:
        grafo.append([])
    else:
        grafo.append([p - 1])

visitados = [False] * len(grafo)

def recorroAPartirDelVerticei(v):
    visitados[v] = True

    for hijo in grafo[v]:
        if not visitados[hijo]:
            recorroAPartirDelVerticei(hijo)


def obtener_componentes_conexas():
    componentes = []

    for i in range(len(grafo)):
        if not visitados[i]:
            componentes.append(i)
            recorroAPartirDelVerticei(i)

    return componentes

def largo_de_camino(v):
    visitados = [False] * len(grafo)

    def dfs(v):
        global largo
        visitados[v] = True
        largo += 1
        for hijo in grafo[v]:
            if not visitados[hijo]:
                dfs(hijo)

    dfs(v)
    return largo


def piramide():
    componentes = obtener_componentes_conexas()
    mesas = -1
    for comp in componentes:
        mesas = max(mesas,largo_de_camino(comp))
    return mesas


print(piramide())