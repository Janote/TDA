C = [4,6,3,2,1]

def caramelos(k,sol_parcial=[]):
    if k == 0:
        return sol_parcial
    else:
        ## Ordeno los caramelos de mayor a menor
        C.sort()
        C.reverse()
        greedy = [None] * k
        i = 0
        while (k != 0):
            greedy[i] = C[i]
            i += 1
            k -= 1 
        return greedy
    

print(caramelos(4))
