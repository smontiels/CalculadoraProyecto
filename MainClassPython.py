##Bibleotecas


##Variables
action = 0;

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