# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# IMOS FACER UN REPASO DOS TIPOS BASICOS DE PYTHON. FAREMOS UN RESUMO QUE VAI SER MOI SIMILIAR AOS TIPOS DE JAVA
# SALVO ALGUNHA EXCEPCION
# Numeros
# Cadea de texto
# Valores booleanos

cadea = "Un texto calquera"
numero = 0o25  # 0x para mumeros hexadecimales, 0o para numeros octales.
booleano = True
print(type(booleano))

print(type(numero))
print(numero)

reais = 3e-15
print(type(reais))

complexo = 2.5 + 8.4j
print(type(complexo))

"""Repaso dos operadores loxicos mais comuns"""

# +-*/
# negacion ~

op = numero ** 2  # expoñente
op = numero // 2  # division enteira
op2 = numero / 2  # division con decimais
resto = numero % 2  # modulo
print(type(op))
print(type(op2))
print(type(resto))

"""Operadores a nivel de bit"""

print(3 & 4)
print(3 | 4)
print(3 ^ 5)
print(~3)
print(3 >> 1)
print(3 << 1)

"""Cadeas"""

c1 = "hola"
c2 = "adeus"

print(c1 + c2)
print(c1 * 4)

"""Operacions booleanas"""

print(True and False)
print(True or False)
print(not True)

print(5 == 6)
print(3 != 6)
print(3 < 6)
print(3 > 6)
print(3 <= 6)
print(3 >= 6)

"""Listas"""

l = [1, 2, 3, 4, 8, -3]
# l = list()
print(type(l))
l2 = [1, 2, 3, True, "Elemento", [5, 6, False]]
print(l2[4][1])
# l[3] = 999
print("-----------")
print(l)
print(l[1:4])
print(l[1:5:2])
print(l[:3])
print(l[1:])
print(l[1::2])

"""TUPLAS"""

t = (1, 2, 3, "Tupla", [1, 2, 3, True])
# t[1]=8 #LAS TUPLAS NO SON EDITABLES, CON LO QUE ESTA LINEA DARIA ERROR.
t2 = 1, 3, 2, 0, "outra tuplas"
t3 = 1,
print(type(t3))
t[4][2] = 100
print(t)
# t[2][3]="x"
# t[3]="outra cousa"
print(t)

c = "abcdefghijklmnñopq"
print(c[2:8])
print(c[
      1:15:2])  # esto quiere decir que coge las letras del 1 al 15 pero solo mostrando el caracter que este cada dos letras, es decir, saltandose uno entre medias. Por eso no aparece ni la "a" ni la "c" ni "e"

"""Diccionarios"""
d = {"Un": 1,
     "Dous": 2,
     "Tres": 3,
     4: "Catro",
     5: "Cinco",
     "Vermello": 0xff0000,
     "Amarelo": 0xffff00,
     "Verde": 0x00ff00,
     "Azul": 0x0000ff}
print(d["Dous"])
print(d[5])

"""Funcions"""


def noseFuncion(parametro, parametro2):
    print("Fai algo con " + str(parametro))
    print("Outra cousa " + parametro2)
    return 1


noseFuncion(1, "dos")


def funcion2(parametro1=2, parametro2="marcos"):
    """En esta funcion imos darlle valores aos parametros por defecto"""
    print(parametro1)
    print(parametro2)


funcion2()

funcion2(parametro1=2, parametro2="julio")


def funcionNumeroParametrosVariable(parametro1, parametro2, *outro):
    """Funcion con número de parametros variable"""
    print(parametro1)
    print(parametro2)
    for parametro in outro:
        print(parametro)


funcionNumeroParametrosVariable(1, 2, 3, 4, 5)


def funcionNumeroParametrosVariableConIdentificador(nome, dni, **outros):
    print("Nome:" + nome)
    print("DNI:" + dni)
    for clave in outros.keys():
        print(clave + ": " + str(outros[clave]))


funcionNumeroParametrosVariableConIdentificador("Marcos", "9436794365W", Edade=34, Sexo="Hombre")


def funcionRetornarVariosValores(x, y):
    """As funcions en python poden retornan mais dun valor"""
    return x * 2, y * 2, 2


t = funcionRetornarVariosValores(5, 1)
print(t[0])
a, b, c = funcionRetornarVariosValores(5, 3)
print(a)
print(b)
print(c)


def saudar(lingua):
    def saudar_gl():
        print("Ola")

    def saudar_es():
        print("Hola")

    def saudar_en():
        print("Hello")

    def saudar_it():
        print("Chiao")

    lingua_funcion = {"es": saudar_es,
                      "gl": saudar_gl,
                      "en": saudar_en,
                      "it": saudar_it}
    return lingua_funcion[lingua]


f = saudar("it")
f()
saudar("en")()

"""Funcions Lambda"""


def numero_par(n):
    return n % 2 == 0


print(numero_par(5))

l = [-3, 4, 5, -6, 7]

l2 = filter(numero_par, l)
print("Pares:")
for elemento in l2:
    print(elemento)

l3 = filter(lambda n: n % 2 == 0, l)
l4 = filter(lambda n: n > 0, l)
print("Maiores que cero:")
for elemento in l3:
    print(elemento)

l5 = [n ** 2 for n in l]
"""Cuadrado de todos los numeros pares"""
l6 = [n ** 2 for n in l if n % 2 == 0]

x = [0, 1, 2, 3]
y = ["a", "b", "c", "d"]

Z = [c * n for n in x for c in y if n > 1]
"""La linea de arriba es lo mismo que:"""

print(Z)

Z = []
for n in x:
    for c in y:
        if n > 1:
            Z.append(n * c)

"""Xeradores"""

x = (n ** 2 for n in l)

print(type(l5))
print(type(x))
print(l5)
print(x)
lista = list(x)
print(lista)
for elemento in x:
    print(elemento)

"""Decoradores"""


def meu_decorador(funcion):
    def nova(*args):
        print("Chamada a funcion ", funcion.__name__)
        retorno = funcion(*args)
        return retorno

    return nova


meu_decorador(saudar)("en")


def saudar2():
    print("Ola")


meu_decorador(saudar2)()


def division(a, b):
    try:
        d = a / b
    except ZeroDivisionError as error:
        print("Ollo, estas dividindo entre 0: " + str(error))
        d = None
    else:
        print("Todo vai ben, non hay excepcions")
    finally:
        print("Executase sempre, haxa ou non excepcion")
        return d


print(division(3, 3))
print(division(3, 0))


def __init__(self, x, y):
    print()


lista = [1, 2, 3]
lista2 = list(lista)
lista.append([1, 2, 3, 4, 5, 6])
lista.extend([1, 2, 3, 4, 5, 6])
print(lista)
print(lista.count(2))
"""print(lista[2].index(1))"""
lista.insert(3, True)
print(lista)
lista.pop(7)
print(lista)
lista.remove(2)
lista.reverse()
print(lista)


def ordena(e):
    return e


lista666 = [3, 8, 1, 9, 4, 6]
lista666.sort(reverse=True)

print(lista666)

tupla = tuple()
diccionario = dict()

"""Métodos dos diccionarios"""

print(d.keys())
print(d.values())

print("Dous" in d)

print(d.pop("Dous"))
print(d)

"""Cadeas"""

cadea = "O patio da miña casa é particular cando chove móllase como os demais patios"
print(cadea.count(" patio"))
print(cadea.find(" patio", 8, 67))

print(cadea.join(" do meu barrio"))
print(cadea.join((" 1 ", " 2 ", " 3 ")))

"""p1 = Persoa ("Luis",20)"""

"""Bases de datos"""

import sqlite3 as dbapi

print(dbapi.apilevel)
print(dbapi.threadsafety)
print(dbapi.paramstyle)

try:

    bbdd = dbapi.connect("bddd.dat")

except dbapi.DatabaseError:
    print("Erro na BD")
else:
    print("Conectado a BD")
    print(bbdd)

try:
    c = bbdd.cursor()
    c.execute("""create table usuarios(dni text, nome text, direccion text)""")
    c.execute("""insert into usuarios values('3333-A','Maria','Canceleiro')""")
    c.execute("""insert into usuarios values('4444-B','Ramona','Madrico')""")
    c.execute("""insert into usuarios values('5555-C','Sandra','Romanof')""")
    bbdd.commit()
except dbapi.DatabaseError as e:
    print("Erro na base de datos: " + str(e))

try:
    c.execute("""select dni, nome, direccion from usuarios""")
    for rexistro in c.fetchall():
        print("DNI: " + rexistro[0])
        print("Nome: " + rexistro[1])
        print("Direccion: " + rexistro[2])
        print(rexistro)
except dbapi.DatabaseError as e:
    print("Erro na base de datos facendo a consulta: " + str(e))

print("\n Select con condicionante \n")

"""Non facer asi"""
try:
    dni = "3333-A"
    c.execute('''select dni, nome, direccion from usuarios where dni ="''' + dni + '"')
    for rexistro in c.fetchall():
        print("DNI: " + rexistro[0])
        print("Nome: " + rexistro[1])
        print("Direccion: " + rexistro[2])
        print(rexistro)
except dbapi.DatabaseError as e:
    print("Erro na base de datos facendo a consulta: " + str(e))

"""Mellor asi"""
print("\n Select con condicionante (forma correcta) \n")

try:
    c.execute('''select dni, nome, direccion from usuarios where dni =?''', (dni,))
    for rexistro in c.fetchall():
        print("DNI: " + rexistro[0])
        print("Nome: " + rexistro[1])
        print("Direccion: " + rexistro[2])
        print(rexistro)
except dbapi.DatabaseError as e:
    print("Erro na base de datos facendo a consulta: " + str(e))

