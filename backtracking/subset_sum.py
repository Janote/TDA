def subsetSum(arr,suma,sol_parcial = [],i = 0):
    if suma == 0:
        return sol_parcial
    elif  suma < 0 or suma > sumaDesde(arr,i):
        return  None          # poda: esta rama no sirve
    else:
        elem = arr[i]
        sol_parcial.append(elem)
        rama1 = subsetSum(arr,suma - elem,sol_parcial,i + 1)
        if rama1 is None:
            sol_parcial.pop()
            return subsetSum(arr,suma,sol_parcial,i+1)
        else:
            return rama1
        
def sumaDesde(arr,i):
    sum = 0 
    while (i < len(arr)):
        sum += arr[i]
        i += 1 
    return sum

print(subsetSum([1,8,7,2,24,9],24))