cadea = "Mi perro me abandono en un bar un lunes por la tarde"

"""6.1: Leer los dos primeros caracteres"""


def exercicio1(cadea):
    return cadea[0:2]


print(exercicio1(cadea))

"""6.2: Leer los 3 ultimos caracteres"""


def exercicio2(cadea):
    return cadea[-3:]


print(exercicio2(cadea))

"""6.5 Leer la cadena al reves"""


def exercicio3(cadea):
    return cadea[::-1]


print(cadea)
print(exercicio3(cadea))

"""Exercicio 6.2.1"""

print(cadea.replace("", ",")[1:-1])


def separarConCadeas(cadea):
    nova = ""
    for c in cadea:
        nova = nova + c + ","

    nova = nova + cadea[-1]

    return nova


print(separarConCadeas(cadea))

"""Exercicio 6.2.2"""

print(cadea.replace(" ", "\_"))

"""Exercicio 6.2.3"""

def ocultarClave(clave):
    return "X"*len(clave)

print(ocultarClave(cadea))