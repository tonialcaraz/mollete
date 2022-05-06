#manejador_archivo = open('/home/toni/programacion/python/mbox.txt')

narchivo = input ('Introduce archivo: ')
try: 
    man_a = open(narchivo)
except:
    print('No se puede abrir el archivo:', narchivo)
    exit()
nlineas = 0 
contador = 0

for linea in man_a:
    linea = linea.rstrip()
    nlineas = nlineas + 1

    if not linea.startswith('Subject:') : #ignoramos lineas que no nos interesan
        continue
    contador = contador + 1
    print (contador, ': ' ,linea)
        


print ('>>> Num. de lineas: ',nlineas)
print ('>>> Ocurrencias: ',contador)