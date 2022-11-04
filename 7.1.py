tupla = (1, 2, 3, 4, 5, 6)
tupla2 = (1, 2, 3, 4, 2)


def exercicio71(tupla):
    ordeada = True
    for numero in range(len(tupla) - 1):
        if tupla[numero] >= tupla[numero + 1]:
            ordeada = False
            break
    return ordeada


if exercicio71(tupla):
    print("Esta ordenada")
else:
    print("Esta desordenada")

if exercicio71(tupla2):
    print("Esta ordenada")
else:
    print("Esta desordenada")
