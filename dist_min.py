import heapq

grafo = {
    "A": [("C", 3), ("F", 2)],
    "B": [("D", 7), ("E", 2), ("F", 6), ("G", 2)],
    "C": [("A", 3), ("F", 2), ("D", 4), ("E", 1)],
    "D": [("C", 4), ("B", 7)],
    "E": [("C", 1), ("F", 3), ("B", 2)],
    "F": [("A", 2), ("C", 2), ("E", 3), ("B", 6), ("G", 5)],
    "G": [("F", 5), ("B", 2)]
}

def dijkstra(grafo, origen="A", destino="B"):
    distancias = {nodo: float("inf") for nodo in grafo}
    predecesores = {nodo: None for nodo in grafo}
    visitados = {nodo: False for nodo in grafo}

    distancias[origen] = 0
    heap = [(0, origen)]

    while heap:
        _, actual = heapq.heappop(heap)

        if visitados[actual]:
            continue

        visitados[actual] = True

        for hijo, distancia in grafo[actual]:
            nueva_distancia = distancias[actual] + distancia

            if nueva_distancia < distancias[hijo] and not visitados[hijo]:
                distancias[hijo] = nueva_distancia
                predecesores[hijo] = actual

                heapq.heappush(heap, (nueva_distancia, hijo))

    if distancias[destino] == float("inf"):
        return []

    camino = []
    it = destino

    while it is not None:
        camino.append(it)
        it = predecesores[it]

    camino.reverse()
    return camino


print(dijkstra(grafo, "A", "B"))