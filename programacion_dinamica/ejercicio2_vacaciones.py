n = int(input())
calendario = list(map(int, input().split()))
M = [[-1] * 3 for _ in range(n)]
 
def vacaciones(dia,anterior):
    if dia == n :
        return 0
    
    if M[dia][anterior] != -1:
        return M[dia][anterior] 
    
    else:
        actividad_actual = calendario[dia]
       
        if (actividad_actual == 3):
            if (anterior == 0):
                M[dia][anterior] =  min(vacaciones(dia+1,1),vacaciones(dia+1,2))
            elif (anterior == 1):
                M[dia][anterior] =  vacaciones(dia+1,2)
            else:
                M[dia][anterior] = vacaciones(dia+1,1)
                
        elif (anterior ==  actividad_actual or actividad_actual == 0): 
            M[dia][anterior] =  1 +  vacaciones(dia+1,0)
        else:
            M[dia][anterior] =  vacaciones(dia+1,actividad_actual)
        return M[dia][anterior]
     
print(vacaciones(0,0))