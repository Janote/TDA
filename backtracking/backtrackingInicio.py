## Tenés una escalera de n escalones. En cada movimiento podés subir 1 o 2 escalones. ¿De cuántas maneras distintas podés llegar arriba? 
## El orden importa.

escaleras = set()

def cantEscaleras(restantes, camino):
    if restantes == 0:
        escaleras.add(tuple(camino))
        return 
    if restantes < 0:
        return
    else:
        camino.append(1)
        cantEscaleras(restantes - 1, camino)
        camino.pop()
        camino.append(2) 
        cantEscaleras(restantes - 2, camino)
        camino.pop()
        
print(cantEscaleras(4,[]))        
print(escaleras)                
