from collections import deque
n = int(input())
visitados = [False] * (n + 1)
grafo = [[] for _ in range(n + 1)]
j = 1 
for _ in range(n - 1):
    n1, n2 = map(int, input().split())

    grafo[n1].append(n2)
    grafo[n2].append(n1) 
seq = list(map(int, input().split()))


def recorridoMisterioso():
    global j
    cola = deque([1])
    visitados[1] = True
    recorrido = [1]
    while cola:
        v = cola.popleft()
        hijos = []

        for hijo in grafo[v]:
            if not visitados[hijo]:
                hijos.append(hijo)

        proximos = seq[j : j + len(hijos)]
        if set(proximos) != set(hijos):
           print("No")
           return False

        j += len(hijos)

        for prox in proximos:
               visitados[prox] = True
               cola.append(prox)
               recorrido.append(prox)

    print("Yes" if recorrido == seq else "No")


recorridoMisterioso()