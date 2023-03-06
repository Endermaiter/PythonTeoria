################################
Exemplo de documentacion con RST
################################

Seccions
--------------------------------

As seccions se marcan con:

* \# con sobreliña para partes
* \* con sobreliña para capitulos
* \= para seccions
* \- para subseccions
* \^ para subsubseccions



Un parágrafo en Restructure text é o bloque mais basico e non necesitamos marcalo de ningunha maneira.

So temos que respetar a tabulación. Para remarcar utilizamos *italica* cun só asterico. Temos outras opcións como a **negriña** con dobre asterisco ou con dobre comilla para codigo: ``este seria o tipo de texto``.

Para facer unha lista

* O primeiro elemento
* O segundo elemento

  Este elemento usa mais dunha liña

  #. Lista autonumerada
  #. Segundo elemento

1. Primeiro Elemento
2. Segundo elemento

Termino (na parte de arriba do texto)
    Definicion do termo, que ten que ser tabulado.

    Pode ter varios parrafos

Outro termo
    Definicion doutro termo

Este é un texto de paragrafo. O seguinte paragrafo é un exemplo de código::

    def funcionNumeroParametrosVariable(parametro1, parametro2, *outro):
        print(parametro1)
        print(parametro2)
        for parametro in outro:
            print(parametro)

    funcionNumeroParametrosVariable(1, 2, 3, 4, 5)

Xa continuamos con texto normal

>>> 1 + 1
2

===== ===== =======
A     B     A and B
===== ===== =======
False False False
True  False False
False True  False
True  True  True
===== ===== =======

+----------------------------+----------------------------+----------------------------+----------------------------+
|Fila de Cabeceira, columna1 | Cabeceira2                 | Cabeceira3                 | Cabeceira 4                |
|(Cabeceira opcional         |                            |                            |                            |
+----------------------------+----------------------------+----------------------------+----------------------------+

Resaltado de texto:
===================

Temos os seguintes recursos:

* Italica - equivalente a *italica*
* Negriña - equivalente a **negriña**
* Literal - equivalente a ``literal``
* Subscript - texto subindice
* Superscript - texto superindice
* Title-reference- para titulos de libros, periodicos e outros materiales.

H\ :sub:`2`\ 0

E = mc\ :sup:`2`

