import heapq
n = int(input())
cantVertices, cantAristas= map(int, input().split())

grafo = {}

for i in range(1,cantVertices +1):
    grafo[i] = []

for _ in range(cantAristas):
    v, w, peso = map(int, input().split())
    grafo[v].append((w,peso))
    grafo[w].append((v,peso))
        

bicis = [None] + list(map(int, input().split()))


print(grafo,bicis)

def juan_y_las_bicis(origen=1):
    bici_actual = bicis[1]
    peso_acumulado = 0 

    heap = [(0, origen)]

    distancias = {nodo: float("inf") for nodo in grafo}

    while heap:
        distancia_actual, actual = heapq.heappop(heap)

        for vecino, peso in grafo[actual]:
            nueva_distancia = distancia_actual * bicis[actual]

            if nueva_distancia < distancias[vecino]:
                distancias[vecino] = nueva_distancia
                anteriores[vecino] = actual
                heapq.heappush(heap, (nueva_distancia, vecino))

    return distancias, anteriores


print(juan_y_las_bicis())