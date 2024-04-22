

# generador de passwords

import random

minusculas = "abcdefghijklmnopqrstuvwxyz"
mayusculas = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
symbols = "@!$%&/*?.,~"

Use_for = minusculas + mayusculas + numeros + symbols
longitud_pass = 15
n_contraseñas = 5
k = 0
almacen =[]
# while k < n_contraseñas:               #Bucle usando While, o más abajo bucle usando For

#     password = "".join(random.sample(Use_for,longitud_pass))
#     print("La contraseña ",k," es: ", password)
#     k = k+1
#     almacen.append(password)


narchivo = input ('Introduce Nombre archivo donde se guardan los passwd : ')
try: 
    man_a = open(narchivo,'x')
except:
    print('No se puede abrir el archivo:', narchivo)
    exit()

for k in range(n_contraseñas):
    password = "".join(random.sample(Use_for,longitud_pass))
    print("La contraseña ",k+1," es: ", password)
    man_a.write(password)
    man_a.write("\n")
    #almacen.append(password)
man_a.close

print("\n")