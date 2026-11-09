
def subset_sum_poda(C, i, j):
    if j < 0 :
        return False 
    if i == 0: 
        return (j == 0)
    else:
        return subset_sum_poda(C, i - 1, j) or subset_sum_poda(C, i - 1, j - C[i])

C = [4,7,2,1]
k = 7
print(subset_sum_poda(C,len(C),k))