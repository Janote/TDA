c = 14
B = [2, 3, 5, 10, 20, 20]
memo = {}

## El ejercicio tiene complejidad O(2^n) y O(n) espacial.
## Pero,
def optiPago(i,c):
    if c <= 0:
        ## Encontre una solucion!
        return (0,0)
    elif i < 0:
        return (float('inf'),float('inf'))
    else:
        elegir =  optiPago(i-1,c-B[i])
        memo[i][c] = min( optiPago(i -1,c), (B[i] + elegir[0] , 1 + elegir[1])) 
        return memo[i][c]
        

print(optiPago(len(B) -1,14))


def optiPagoBU(i,c):
    if c <= 0:
        return (0,0)
    else:
        

   
