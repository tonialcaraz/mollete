import random


def adivina_el_numero_computadora(x):   # siendo x el valor más alto del rango al que pertenezca el num a adivinar

    print("=====================================")
    print("       Bienvenide al juego !         ")
    print("=====================================")
    print("Selecciona un numero entre 1 y {x} para que la computer lo adivine: ")

    limite_inf = 1      #[1,x]
    limite_sup = x 

    respuesta =""
    while respuesta !="c":
        # generar prediccion
        if limite_inf != limite_sup: 
            prediccion = random.radint(limite_inf,limite_sup)
        else: 
            prediccion = limite_inf # tb podria ser el limmite sup

    # obtener respuesta del usuario
    respuesta = input(f"Mi prediccion es {prediccion}, Si es muy alta ingresa (A)\n Si es muy baja ingresa (B)\n Si es correcta ingresa (C) :").lower() # al meter lower() siempre obtendremos minusculas

    if respuesta == "a":
        limite_sup = prediccion - 1
        #  Intervalo inicial: [1,10]     
        #  prediccion: 6
        #  Respuesta: "a" (6 es muy alto, entonces esta por debajo de 6, por eso "prediccion -1")
        #  entonces rebajamos intervalo: [1,5]
    elif respuesta == "b":
        
