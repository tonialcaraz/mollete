# Ejercicio 3: Escribe un programa que solicite una puntuacion entre 0.0 y 1.0. Si la
# puntuacion está fuera de ese rango, muestra un mensaje de error. Si la puntuacion
# está entre 0.0 y 1.0, muestra la calificacion usando la tabla siguiente:

# Puntuacion
# >= 0.9 
# >= 0.8
# >= 0.7
# >= 0.6
# < 0.6

# Calificacion
# Sobresaliente
# Notable
# Bien
# Suficiente
# Insuficiente

# Introduzca puntuacion: 0.95
# Sobresaliente

# Introduzca puntuacion: perfecto
# Puntuacion incorrecta

# Introduzca puntuacion: 10.0
# Puntuacion incorrecta

# Introduzca puntuacion: 0.75
# Bien

# Introduzca puntuacion: 0.5
# Insuficiente

try :
    puntuacion = float(input ('introduce la puntuacion :'))

    if puntuacion >= 0.0 and puntuacion <= 1.0 : 

       if puntuacion < 0.6 :
           resultado = 'Insuficiente'
       elif puntuacion >= 0.6 and puntuacion < 0.7 :
           resultado = 'Suficiente'
       elif puntuacion >= 0.7 and puntuacion < 0.8 :
           resultado = 'Bien'
       elif puntuacion >= 0.8 and puntuacion < 0.9 :  
           resultado = 'Notable'
       elif puntuacion >= 0.9 and puntuacion <= 1.0 :  
           resultado = 'Sobresaliente'
    else :
        resultado = 'Puntuacion incorrecta'

    print (resultado)

except : 
   print ('puntuacion incorrecta excep\n')
    




