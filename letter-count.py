palabra = input ('introduce una palabra :')
letras = []
n=0
for letra in palabra:
    letras.insert(n,letra)
    n=n+1
print(letras,'\n')
print(palabra,'tiene',len(palabra),'caracteres')
i=0
for i in range(len(letras)):
    print ('\n carácter número:',i+1,'=> ',letras[i])        
    i=i+1


# esto va a ser 
# un comentario