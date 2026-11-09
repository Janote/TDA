from math import factorial


def pascalito(f,c):
    if (f == 0 or c == 0):
        return 1 
    else:
        return pascalito(f-1,c) + pascalito(f,c-1)
print(pascalito(4,3))


def formula_cerrada_pascal(f,c):
    numerador = factorial(f + c)
    denominador = factorial(f) * factorial(c)
    return numerador // denominador

for f in range(6):
    for c in range(6):
        resultado1 = pascalito(f, c)
        resultado2 = formula_cerrada_pascal(f, c)

        assert resultado1 == resultado2
        print(f"OK: ({f}, {c}) -> {resultado1} == {resultado2}")