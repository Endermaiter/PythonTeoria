"""
JAVA CONDICIONALES
if(condicion){
instruccion1;
instruccion2;
...;
}else{
instruccion1;
instruccion2;
    }
    """

"""PYTHON CONDICIONALES"""

var = 2
if var == 2:
    print("AJAJSJDADJFj")
    print("AJAJSJDADJFj")
    if var == 1:
        print("AJAJSJDADJFj")
    else:
        print("marcos")
else:
    print("AJAJSJDADJFj")
    print("AJAJSJDADJFj")

"""int variable = (condicion) ? valor1: valor2;"""

variable = "pan" if var % 2 == 0 else "Impar"

"""WHILE"""

numero = 0
while numero < 5:
    print("Numero: " + str(numero))
    numero += 1
numero = 0
while True:
    numero += 1
    print("Numero: " + str(numero))
    if numero == 5:
        break

"""FOR"""

coleccion = [1, 2, 3, 4, 5, 9]

for numero in coleccion:
    print(numero)

    """for(i=0;i<5;i++)"""

for i in range(0, 5, 1):
    print(i)

d = {1: "un",
     2: "dous",
     3: "tres"}

for valor in d.values():
    print(valor)

for valor in d.keys():
    print(valor)
