def ejercitoDelRey(n):
    M = [None] * (n + 1 ) 
    M[0] = 1 
    M[1] = 1
    def calcularEjercito(n):
        if M[n] != None:
            return M[n]
        else:
            M[n] = calcularEjercito(n-1) + calcularEjercito(n-2)
            return M[n]     
    calcularEjercito(n)

ejercitoDelRey(4)


## La complejidad temporal es la cantidad de estados posibles por el costo en cada uno de sus
## estados, en este caso hay 𝑛 estados posibles si llamamos a 𝑓(𝑛) y en cada estado se hace trabajo
## 𝑂(1) con lo cual nos queda una complejidad lineal en 𝑂(𝑛).
