p = [3, 6, 10]
n = len(p)
M = [[None] * (n + 1) for _ in range(n)]

def astroTrade(i, cantObjetos):
    if i == n:
        return 0 if cantObjetos == 0 else float("-inf")

    if M[i][cantObjetos] is not None:
        return M[i][cantObjetos]

    comprar = astroTrade(i + 1, cantObjetos + 1) - p[i]
    no_operar = astroTrade(i + 1, cantObjetos)

    vender = float("-inf")
    if cantObjetos > 0:
        vender = astroTrade(i + 1, cantObjetos - 1) + p[i]

    M[i][cantObjetos] = max(comprar, no_operar, vender)
    return M[i][cantObjetos]

print(astroTrade(0, 0))  


# f(i, c) =
#     -infinito, si i = n y c != 0

#     0, si i = n y c = 0

#     max{f(i+1, 1) - p[i], f(i+1, 0)},
#         si 0 <= i < n y c = 0

#     max{f(i+1, c+1) - p[i], f(i+1, c), f(i+1, c-1) + p[i]},
#         si 0 <= i < n y c > 0
