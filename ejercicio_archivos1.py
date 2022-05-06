#manejador_archivo = open('/home/toni/programacion/python/mbox.txt')

# narchivo = input ('Introduce archivo: ')
# try: 
#     man_a = open(narchivo)
# except:
#     print('No se puede abrir el archivo:', narchivo)
#     exit()

man_a = open('/home/toni/programacion/python/mbox.txt')

decimal     = 0
acumulado   = 0
lineas      = 0
for linea in man_a:
    
    if linea.find('X-DSPAM-Confidence:') == -1 : #ignoramos lineas que no nos interesan
        continue
    linea = linea.rstrip()
    decimal = float(linea[20:])
    acumulado = acumulado + decimal
    lineas = lineas + 1
print ('promedio : ',acumulado/lineas)
print ('lineas: ' ,lineas)

     


