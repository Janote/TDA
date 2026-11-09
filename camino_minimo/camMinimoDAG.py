from collections import deque
# Si existe un orden topológico, el grafo dirigido es acíclico (DAG).
grafo = {
    "A": [("B", 3), ("C", 6)],
    "B": [("D", 4), ("E", 2)],
    "C": [("D", 2), ("F", 5)],
    "D": [("E", 1), ("F", 3)],
    "E": [("G", 4)],
    "F": [("G", 2)],
    "G": []
}

def orden_topologico(grafo):
    grado_entrada = {nodo: 0 for nodo in grafo}

    for nodo in grafo:
        for v, _ in grafo[nodo]:
            grado_entrada[v] += 1


    cola = deque(
        v for v in grafo
        if grado_entrada[v] == 0
    )

    orden = []

    while cola:
        u = cola.popleft()
        orden.append(u)

        for v, peso in grafo[u]:
            grado_entrada[v] -= 1
            if grado_entrada[v] == 0:
                cola.append(v)

    if len(orden) != len(grafo):
        raise ValueError("El grafo tiene ciclos")

    return orden

orden_topologico(grafo)

def caminos_minimos_dag(grafo, s):
    orden = orden_topologico(grafo)

    d = [float("inf")] * len(grafo)
    predecesor = [None] * len(grafo)
    d[s] = 0

    for u in orden:
        for v, peso in grafo[u]:
            # Relajar la arista u → v
            if d[u] != float("inf") and d[v] > d[u] + peso:
                d[v] = d[u] + peso
                predecesor[v] = u

    return d, predecesor