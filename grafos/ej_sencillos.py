grafo = [
    [1],
    [2],
    [3],
    [],
    [3],
    [2]
]


def recorrido_dfs(grafo, inicio):
    visitados = [False] * len(grafo)
    recorrido = []

    def dfs(v):
        visitados[v] = True
        recorrido.append(v)

        for hijo in grafo[v]:
            if not visitados[hijo]:
                dfs(hijo)

    dfs(inicio)
    return recorrido


def existe_camino(grafo, inicio, buscado):
    visitados = [False] * len(grafo)

    def dfs(v):
        visitados[v] = True

        if v == buscado:
            return True

        for hijo in grafo[v]:
            if not visitados[hijo]:
                if dfs(hijo):
                    return True

        return False

    return dfs(inicio)


def recorroAPartirDelVerticei(grafo, v, visitados):
    visitados[v] = True

    for hijo in grafo[v]:
        if not visitados[hijo]:
            recorroAPartirDelVerticei(grafo, hijo, visitados)


def obtener_componentes_conexas(grafo):
    visitados = [False] * len(grafo)
    componentes = []

    for i in range(len(grafo)):
        if not visitados[i]:
            componentes.append(i)
            recorroAPartirDelVerticei(grafo, i, visitados)

    return componentes

def largo_de_camino(grafo,v):
    largo = 0
    visitados = [False] * len(grafo)

    def dfs(v):
        nonlocal largo
        visitados[v] = True
        largo += 1
        for hijo in grafo[v]:
            if not visitados[hijo]:
                dfs(hijo)

    dfs(v)
    return largo

    
def get_predecesores(grafo):
    visitados = [False] * len(grafo)
    padres = [[] for _ in range(len(grafo))]

    def dfs(v):
        visitados[v] = True
        for hijo in grafo[v]:
            padres[hijo].append(v)

            if not visitados[hijo]:
                dfs(hijo)

    comp_conexas = obtener_componentes_conexas(grafo)

    for representante in comp_conexas:
        if not visitados[representante]:
            dfs(representante)

    return padres



grafo2 = [[1],[],[3],[1]]
grafo3 = [[1], []]

def piramide(grafo):
    componentes = obtener_componentes_conexas(grafo)
    mesas = -1
    for comp in componentes:
        mesas = max(mesas,largo_de_camino(grafo,comp))
    return mesas


print(piramide(grafo))