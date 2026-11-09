import heapq

grafo = {
    "A": [("B", 6), ("C", 2)],
    "B": [("D", 2), ("E", 7)],
    "C": [("B", 1), ("D", 5)],
    "D": [("E", 3)],
    "E": []
}


def dijkstra(grafo, origen):
    distancias = {nodo: float("inf") for nodo in grafo}
    anteriores = {nodo: None for nodo in grafo}

    distancias[origen] = 0
    heap = [(0, origen)]

    while heap:
        distancia_actual, actual = heapq.heappop(heap)

        if distancia_actual > distancias[actual]:
            continue

        for vecino, peso in grafo[actual]:
            nueva_distancia = distancia_actual + peso

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = actual
                heapq.heappush(heap, (nueva_distancia, vecino))

    return distancias, anteriores

def entrega_de_pedidos(grafo, origen="A", destino="D"):
    distancias, predecesores = dijkstra(grafo, origen)
    return distancias[destino]


def llegar_a_facultad(grafo, origen="A", destino="E"):
    distancias, ancestros  = dijkstra(grafo,origen)
    camino = [] 
    nodo = destino
    
    while nodo != origen:
        camino.append(nodo)
        nodo = ancestros[nodo]
    camino.append(nodo)
    camino.reverse()

    return camino, distancias[destino] 


print(llegar_a_facultad(grafo))


## Lo que pasa es crear un 
def findCheapestPrice(n, flights, src, dst, k):
    grafox = {}
    distancias = {} 
    for i in range(n):
        grafox[i] = []
        distancias[i] = k , float('inf')

    for flight in flights:
        xfrom = flight[0]
        to = flight[1]
        cost = flight[2]
                        
        grafox[xfrom].append((to,cost))

        
        distancias[origen][1] = 0
        heap = [(0, origen)]

        while heap or k >= 0:
            (  node_k ,distancia_actual), actual = heapq.heappop(heap)

            # Esta entrada quedó vieja porque encontramos un camino mejor.
            if distancia_actual > distancias[actual]:
                continue

            for vecino, peso in grafo[actual]:
                nueva_distancia = distancia_actual + peso

                if nueva_distancia < distancias[vecino]:
                    distancias[vecino] = nueva_distancia
                    heapq.heappush(heap, (nueva_distancia, vecino))

    if distancias[dst] == float('inf'):
        raise ValueError("No se encontró un camino válido")
    
    return distancias


n = 4
flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
src = 0
dst = 3
k = 1

findCheapestPrice(n,flights,src,dst,k)