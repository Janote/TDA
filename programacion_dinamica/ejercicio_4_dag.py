from collections import deque

dag = {
    0: [1, 2,5],
    1: [3],
    2: [3, 4],
    3: [4],
    4: [],
    5: [] 
}

def orden_topologico():
    grados = {}
    for v in dag:
        grados[v] = 0

    for v in dag:
        for w in dag[v]:
            grados[w] += 1 
    
    q = deque()
    for v in dag:
        if grados[v] == 0:
            q.append(v)
    res = []

    while q :
        v = q.pop()
        res.append(v)
        for w in dag[v]:
            grados[w] -= 1
            if grados[w] == 0:
                q.append(w)
    return res


print(orden_topologico())
## Este algoritmo tiene complejidad Temporal O(N + M)
def contarCaminos(s, t):
    memo = {}

    def resolver(nodo):
        if nodo == t:
            return 1

        if nodo in memo:
            return memo[nodo]

        cantidad = 0
        for hijo in dag[nodo]:
            cantidad += resolver(hijo)

        memo[nodo] = cantidad
        return cantidad

    return resolver(s)


print(contarCaminos(0, 4))  # 5

def contar_caminos_bottom_up(dag, s, t, orden):
    caminos = {nodo: 0 for nodo in dag}
    caminos[t] = 1

    for nodo in reversed(orden):
        if nodo == t:
            continue

        for hijo in dag[nodo]:
            caminos[nodo] += caminos[hijo]

    return caminos[s]

ord = orden_topologico()
print(contar_caminos_bottom_up(dag,0,4,ord))  # 5
