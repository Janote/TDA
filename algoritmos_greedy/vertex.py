def calcular_grados(grafo):
    return {v: len(grafo[v]) for v in grafo}


def sacar_aristas(grafo, v):
    grafo[v].clear()

    for vertice in grafo:
        grafo[vertice].discard(v)


def vertex_cover_greedy(grafo):
    grados = calcular_grados(grafo)
    cant_vertices_sacados = 0

    while any(grado > 0 for grado in grados.values()):
        # Elegimos el vértice con mayor grado actual.
        vertice = max(grados, key=grados.get)

        sacar_aristas(grafo, vertice)
        cant_vertices_sacados += 1
        grados = calcular_grados(grafo)

    return cant_vertices_sacados


grafo = {
    0: {1},
    1: {0},
    2: set(),
    3: set()
}

print(vertex_cover_greedy(grafo))  # 1