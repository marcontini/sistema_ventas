#Programa encargado de generar una matriz cuadrada del tamaño especificado en la variable num
#El programa va a crear un archivo de texto el cual su información va a tener un formato .csv
lst_matriz = []
num = 50
for i in range(num):
    str_aux = '' 
    for j in range(num):
        if j==num-1:
            str_aux += '0'
        else:
            str_aux += '0,'
            
    str_aux += '\n'
    lst_matriz.append(str_aux)

print(lst_matriz)

arch = open('asientos.txt','w')
for i in lst_matriz:
    arch.write(i)
arch.close()



