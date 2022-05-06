fsal = open('salida.txt', 'w')

linea1 = "Aquí está el zarzillo,\n"
fsal.write(linea1)

fsal.write("segunda línea\n")
fsal.close

fsal =  open('salida.txt')
print (fsal.read())