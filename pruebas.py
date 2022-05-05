# pruebas python

str = 'X-DSPAM_Confidence:0.8475'

posicion = str.find(':') + 1
print (posicion)
numero = float(str[posicion:])

print (numero)