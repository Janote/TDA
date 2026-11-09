estaciones = [0, 80, 140, 200, 280, 350]
autonomia = 150
destino = 400

def ruta_eficiente():
    cant_paradas = 0 
    ult_parada = 0 
    estaciones_a_parar = [0] 

    while( estaciones[ult_parada] + autonomia < destino):
        proxima_parada = ult_parada + 1
        
        while(estaciones[ult_parada]  + autonomia >= estaciones[proxima_parada]):
            proxima_parada += 1
        
        ult_parada  = proxima_parada  - 1
        cant_paradas += 1 
        estaciones_a_parar.append(estaciones[ult_parada])

    estaciones_a_parar.append(estaciones[len(estaciones) - 1])
    return estaciones_a_parar

print(ruta_eficiente())