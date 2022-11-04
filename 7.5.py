listaEnteiros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
print(listaEnteiros)

print("PUNTO 1")


def primo(n):
    primo = True
    for num in range(2, n):
        if n % num == 0:
            primo = False
    return primo


print("Primo: " + str(primo(11)))


def primoLista(l):
    return [n for n in l if primo(n)]


print("Lista de primos: " + str(primoLista(listaEnteiros)))

print("PUNTO 2")

suma = 0
for numeros in listaEnteiros:
    suma = suma + numeros

promedio = suma / len(listaEnteiros)
print("O sumatorio da lista é " + str(suma))
print("A media da lista é " + str(promedio))

print("PUNTO 3")


def factorialNumero(n):
    factorial = 1
    for multiplicador in range(1, n + 1):
        factorial = factorial * multiplicador
    return factorial


"""Las siguientes def hacen exactamente lo mismo pero con diferente forma de codificarlo."""

def factorialLista(l):
    return [factorialNumero(n) for n in l]

def factorialLista2(l):
    listaFactorial = list()
    for n in l:
        listaFactorial.append(factorialNumero(n))
    return listaFactorial


print("Factorial dunha lista")
print(factorialLista(listaEnteiros))
print(factorialLista2(listaEnteiros))
