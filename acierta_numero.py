import random


def adivina_el_numero(x):   # siendo x el valor más alto del rango al que pertenezca el num a adivinar

    print("=====================================")
    print("       Bienvenide al juego !         ")
    print("=====================================")
    print("Adivina el número generado por el computer\n")

    numero_aleatorio = random.randint(1, x) # Numero aleatorio entre 1 y x (ambos incluidos)

    prediccion = 0

    while prediccion != numero_aleatorio:
        prediccion = int(input(f"Adivina un número entre 1 y {x}: ")) # cadena f-string -> con la f sustituiremos las variables entre llaves {}
                                                                      # ponemos int() para convertir la cadena string a entero (numerico)
        if prediccion < numero_aleatorio:
            print ("Intenta otra vez, este número es muy pequeño\n")
        elif prediccion > numero_aleatorio:
            print("Intenta otra vez, este número es muy grande\n")

    print(f"Felicidades, adivinaste el número {numero_aleatorio}")


adivina_el_numero(10)


