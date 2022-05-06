# romeo

# Escribir un programa para abrir el archivo romeo.txt y leerlo línea
# por línea.
# 
# Para cada línea, dividir la línea en una lista de palabras utilizando la función split. 
# Para cada palabra, revisar si la palabra ya se encuentra previamente en la lista. 
# Si la palabra no está en la lista, agregarla a la lista. 
# 
# Cuando el programa termine, ordenar e imprimir las palabras resultantes en orden alfabético.

narchivo = input('Introduce el nombre de archivo: ')

try:
    man_a = open(narchivo)

except:

    print('No se puede abrir el archivo:', narchivo)
    exit()

for linea in man_a:
     lista = linea.rstrip().split(' ')
     print (lista)   