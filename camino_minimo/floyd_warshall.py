def floyd_warshall(grafo):
    nodos = list(grafo.keys())
    dist = {
        u: {v: float("inf") for v in nodos}
        for u in nodos
    }

    # Distancia de un nodo a sí mismo
    for u in nodos:
        dist[u][u] = 0

    # Inicializar las aristas
    for u in grafo:
        for v, peso in grafo[u]:
            dist[u][v] = min(dist[u][v], peso)

    # Floyd-Warshall
    for k in nodos:
        for i in nodos:
            for j in nodos:
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    return dist