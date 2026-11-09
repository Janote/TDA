def mergeSort(arr):
    if len(arr) <= 1:
        return arr 
    mitad = len(arr) // 2
    mitad_izq = mergeSort(arr[:mitad])
    mitad_der = mergeSort(arr[mitad:])
    arr = merge(mitad_izq,mitad_der)
    return arr 
def merge(izq,der):
    i = 0 
    j = 0 
    res = [] 
    while i < len(izq) and j < len(der):
        if izq[i] < der[j]:
            res.append(izq[i])
            i+= 1 
        else:
            res.append(der[j])
            j += 1
    res += izq[i:]
    res += der[j:]
    return res 
   
      