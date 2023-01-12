##Bibleotecas
import math
import numpy as np

##Variables
action = 0

##Método principal
while action != 10:

##Menú
    print("\"Bienvenido a la Calculadora en Python\"")
    print("Las opciones disponibles son: "
          "\n\n1)Sumar"
          "\n2)Restar"
          "\n3)Multiplicar"
          "\n4)Dividir"
          "\n5)Raíz Cudrada"
          "\n6)Exponente"
          "\n\n7)Seno"
          "\n8)Coseno"
          "\n9)Tangente"
          "\n\n10)Salir"
          "\n")

    try:
        action = int(input("¿Qué operación desea realizar? "))
    except:
        print("¡Debes introducir una opción entre 1 - 10!")

    ## ******** SUMA ********
    if action == 1:
        salirFlujoSecundario = False
        while salirFlujoSecundario != True:

            print("Elegiste Suma \n*************")

            try:
                numeroUno = int(input("Introduce el primer número: "))
            except:
                print("Sólo valores numéricos")
            try:
                numeroDos = int(input("Introduce el segundo número: "))
            except:
                print("Sólo valores numéricos")
            print("\nEl resultado fue: ", numeroUno + numeroDos)

            respuesta = 0

            try:
                respuesta = int(input("¿Deseas realizar otra operación Sí(1) / No(Cualquier caracter)?: "))
            except:
                print("Sólo números como respuestas")

            if respuesta != 1 :
                salirFlujoSecundario = True

    ## ******RESTA********
    if action == 2:
        salirFlujoSecundario = False
        while salirFlujoSecundario != True:

            print("Elegiste Resta \n*************")

            try:
                numeroUno = int(input("Introduce el primer número: "))
            except:
                print("Sólo valores numéricos")
            try:
                numeroDos = int(input("Introduce el segundo número: "))
            except:
                print("Sólo valores numéricos")
            print("\nEl resultado fue: ", numeroUno - numeroDos)

            respuesta = 0

            try:
                respuesta = int(input("¿Deseas realizar otra operación Sí(1) / No(Cualquier caracter)?: "))
            except:
                print("Sólo números como respuestas")

            if respuesta != 1:
                salirFlujoSecundario = True

    ## ******Multiplicar********
    if action == 3:
        salirFlujoSecundario = False
        while salirFlujoSecundario != True:

            print("Elegiste Multiplicar \n*************")

            try:
                numeroUno = int(input("Introduce el primer número: "))
            except:
                print("Sólo valores numéricos")
            try:
                numeroDos = int(input("Introduce el segundo número: "))
            except:
                print("Sólo valores numéricos")
            print("\nEl resultado fue: ", numeroUno * numeroDos)

            respuesta = 0

            try:
                respuesta = int(input("¿Deseas realizar otra operación Sí(1) / No(Cualquier caracter)?: "))
            except:
                print("Sólo números como respuestas")

            if respuesta != 1:
                salirFlujoSecundario = True

    ## ******Dividir********
    if action == 4:
        salirFlujoSecundario = False
        while salirFlujoSecundario != True:

            print("Elegiste Dividir \n*************")

            try:
                numeroUno = float(input("Introduce el primer número: "))
            except:
                print("Sólo valores numéricos")
            try:
                numeroDos = float(input("Introduce el segundo número: "))
            except:
                print("Sólo valores numéricos")
            print("\nEl resultado fue: ", numeroUno / numeroDos)

            respuesta = 0

            try:
                respuesta = int(input("¿Deseas realizar otra operación Sí(1) / No(Cualquier caracter)?: "))
            except:
                print("Sólo números como respuestas")

            if respuesta != 1:
                salirFlujoSecundario = True

    ## ******Raíz cuadrada********
    if action == 5:
        salirFlujoSecundario = False
        while salirFlujoSecundario != True:

            print("Elegiste Raíz Cuadrada \n*************")

            try:
                numeroUno = float(input("Introduce un número para obtener su raíz: "))
            except:
                print("Sólo valores numéricos")
            print("\nEl resultado fue: ", math.sqrt(numeroUno))

            respuesta = 0

            try:
                respuesta = int(input("¿Deseas realizar otra operación Sí(1) / No(Cualquier caracter)?: "))
            except:
                print("Sólo números como respuestas")

            if respuesta != 1:
                salirFlujoSecundario = True

    ## ******Exponente********
    if action == 6:
        salirFlujoSecundario = False
        while salirFlujoSecundario != True:

            print("Elegiste Exponente \n*************")

            try:
                numeroUno = float(input("Introduce el número BASE: "))
            except:
                print("Sólo valores numéricos")
            try:
                numeroDos = float(input("Introduce el EXPONENTE: "))
            except:
                print("Sólo valores numéricos")
            print("\nEl resultado fue: ", pow(numeroUno,numeroDos))

            respuesta = 0

            try:
                respuesta = int(input("¿Deseas realizar otra operación Sí(1) / No(Cualquier caracter)?: "))
            except:
                print("Sólo números como respuestas")

            if respuesta != 1:
                salirFlujoSecundario = True

    ## ******Seno********
    if action == 7:
        salirFlujoSecundario = False
        while salirFlujoSecundario != True:

            print("Elegiste Seno \n*************")

            try:
                numeroUno = float(input("Introduce un número para calcula el seno: "))
            except:
                print("Sólo valores numéricos")
            print("\nEl resultado fue: ", np.sin(np.radians(numeroUno)))

            respuesta = 0

            try:
                respuesta = int(input("¿Deseas realizar otra operación Sí(1) / No(Cualquier caracter)?: "))
            except:
                print("Sólo números como respuestas")

            if respuesta != 1:
                salirFlujoSecundario = True

    ## ******Coseno********
    if action == 8:
        salirFlujoSecundario = False
        while salirFlujoSecundario != True:

            print("Elegiste Coseno \n*************")

            try:
                numeroUno = float(input("Introduce un número para calcula el coseno: "))
            except:
                print("Sólo valores numéricos")
            print("\nEl resultado fue: ", np.cos(np.radians(numeroUno)))

            respuesta = 0

            try:
                respuesta = int(input("¿Deseas realizar otra operación Sí(1) / No(Cualquier caracter)?: "))
            except:
                print("Sólo números como respuestas")

            if respuesta != 1:
                salirFlujoSecundario = True

    ## ******Tangente********
    if action == 9:
        salirFlujoSecundario = False
        while salirFlujoSecundario != True:

            print("Elegiste Tangente \n*************")

            try:
                numeroUno = float(input("Introduce un número para calcula la tangente: "))
            except:
                print("Sólo valores numéricos")
            print("\nEl resultado fue: ", np.tan(np.radians(numeroUno)))

            respuesta = 0

            try:
                respuesta = int(input("¿Deseas realizar otra operación Sí(1) / No(Cualquier caracter)?: "))
            except:
                print("Sólo números como respuestas")

            if respuesta != 1:
                salirFlujoSecundario = True