manejador_archivo = open('/home/toni/programacion/python/mbox.txt')

nlineas = 0 
contador = 0

for linea in manejador_archivo:
    linea = linea.rstrip()
    nlineas = nlineas + 1

    if linea.find('@uct.ac.za') == -1 : #ignoramos lineas que no nos interesan
        continue
    contador = contador + 1
    print (contador, ': ' ,linea)
        


print ('>>> Num. de lineas: ',nlineas)
print ('>>> Ocurrencias: ',contador)