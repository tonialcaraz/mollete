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
