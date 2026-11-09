grafo = {
    "A": [("B", 6), ("C", 4), ("D", 5)],
    "B": [("E", -1)],
    "C": [("B", -2), ("E", 3)],
    "D": [("C", -2), ("F", -1)],
    "E": [("F", 3)],
    "F": []
}

def bellman_ford():
    distancias = {nodo: float("inf") for nodo in grafo}
    predecesores = {nodo: None for nodo in grafo}

    distancias["A"] = 0

    for _ in range(len(grafo) - 1):
        for vertice in grafo:
            modified = False
            for vecino, peso in grafo[vertice]:
                nueva_distancia = distancias[vertice] + peso

                if nueva_distancia < distancias[vecino]:
                    modified = True
                    distancias[vecino] = nueva_distancia
                    predecesores[vecino] = vertice
        if not modified:
                break            
    return distancias, predecesores


print(bellman_ford())

