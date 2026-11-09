numeros = {
    "2": ["a", "b", "c"],
    "3": ["d", "e", "f"],
    "4": ["g", "h", "i"],
    "5": ["j", "k", "l"],
    "6": ["m", "n", "o"],
    "7": ["p", "q", "r", "s"],
    "8": ["t", "u", "v"],
    "9": ["w", "x", "y", "z"]
}

sol_parcial = []
soluciones_validas = []

def letterCombinations(sol_parcial, digits, i=0):
    if i == len(digits):
        soluciones_validas.append("".join(sol_parcial))
    else:
        digito = digits[i]

        for caracter in numeros[digito]:
            sol_parcial += caracter
            letterCombinations(sol_parcial, digits, i + 1)
            sol_parcial.pop()

digits = "23"
letterCombinations(sol_parcial, digits)
print(soluciones_validas)