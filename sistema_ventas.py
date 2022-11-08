def es_letra(x):
    return ('a'<=x<='z' or 'A'<=x<='Z' or x in 'áéíóúÁÉÍÓÚ')

def crear_lista(arch):
    #Creo una variable lst_arch a la cual le voy a otorgar el valor que retorna pasar el archivo
    #arch por la funcion readlines
    lst_arch = arch.readlines()
    
    #Creo tres variables
    lst_res = [] #lista que voy a retornar una vez terminada la funcion
    lst_aux = [] #lista auxiliar en la cual voy a almacenar datos para luego appendear esta lista en lst_res
    str_aux = '' #string auxiliar el cual va a almacenar los datos que van a ir dentro de lst_aux
    for fila in lst_arch: #le otorgo a la variable fila mediante un for los elementos de la lista lst_arch
        for j in fila: #le otorgo a la variable j mediante un for los elementos de la variable fila
            if j!=',' and j!='\n': #veo si j es distinto de ',' y '\n' ya que estoy queriendo separar los valores de un archivo de tipo csv
                str_aux += j #si j es distinto de ',' y '\n' lo agrego al str_aux
            else: #en cambio si j es igual a ',' o a '\n' 
                lst_aux.append(str_aux) #appendeo el str_aux a la lst_aux
                str_aux = '' #vacio el str_aux para usarlo nuevamente
        
        #Ya terminado el for para armar la lst_aux
        lst_res.append(lst_aux) #appendeo la lst_aux a lst_res
        lst_aux = [] #vacio lst_aux para usarla nuevamente
    
    return lst_res #retorno la lst_res

def ordenar(lst):
    for i in range(0,len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i][0]>lst[j][0]:
                lst[i], lst[j] = lst[j], lst[i]
        
    return lst

def num(cont,long):
    num_res = ''
    num_aux = str(cont)
        
    for i in range(0,long-len(num_aux)):
        num_res += '0'
    num_res += num_aux
        
    return num_res #retorna el numero modificado

def print_matriz():
    arch = open('asientos.txt','r') #abro el archivo 'asientos.txt' en modo lectura ('r')
    lst_matriz = crear_lista(arch) #paso el archivo (arch) por la funcion crear_lista() y lo que retorne se lo asigno a lst_matriz
    len_matriz = len(lst_matriz) #le otorgo a la variable len_matriz el valor de la longitud de lst_matriz
      
    for fila in range(len_matriz):
        if len(str(fila))==1:
            print(f'fila {num(str(fila),2)} ',end='- ')
        else:
            print(f'fila {num(str(fila),2)} ',end='- ')
        for columna in lst_matriz[fila]:  
            print(columna, end='    ')                   
        print()
    
    print()

def guardar_asientos(lst):
    #Esta funcion se va a encargar de recibir la lista de los asientos modificada dsps de generar una venta
    #y guardar la informacion de la lista en el archivo asientos, al guardarla se va a sobreescribir la
    #informacion que tenia antes dandole lugar a la nueva informacion
    print('\nGuardando asiento...')
    lst_res = [] #Creo una lista vacia llamada lst_res en la cual voy a agregar la nueva informacion de todas las filas de los asientos en formato .csv
    for i in lst: #Recorro la lista de asientos pasada por parametro asignandole a i el valor de cada sublista de lst
        str_aux = '' #Creo un string vacio llamado str_aux al cual le voy a ir agregando la informacion de cada fila en formato .csv
        for j in range(len(i)): #Recorro el largo de la sublista i
            if j==len(i)-1: #Me fijo si j es igual el ultimo lugar de i para saber si tengo q agregar un \n para terminar la fila y hacer el salto de linea en el archivo
                str_aux += str(i[j])+'\n'
            else: #Si no es el ultimo lugar al str_aux le agrego una coma para separar los valores que le siguen en la misma fila
                str_aux += str(i[j])+','
                    
        lst_res.append(str_aux) #Una vez armado el str_aux, o sea, la fila, appendeo esta a lst_res y empiezo devuelta hasta recorrer todo lst
    
    #Una vez termino de armar lst_res guardo la informacion de cada elemento de lst_res en el archivo asientos.txt
    arch = open('asientos.txt','w') #Primero abro el archivo en modo escritura
    for i in lst_res: #Luego recorro la lista lst_res para sacar el valor de cada fila el cual se lo otorgo a la variable i
        arch.write(i) #Le escribo al archivo la variable i, o sea, va a ir escribiendole cada fila al asiento
    
    #Termino de escribir la info en el archivo y prineto un aviso
    print('Asiento guardado!')
    arch.close() #Cierro el archivo de asientos
    
def venta(): #Funcion venta donde voy a pedir todos los datos necesarios para generar la venta
    arch_asientos = open('asientos.txt','r') #Abro el archivo asientos
    matriz = crear_lista(arch_asientos) #Creo una variable llamada matriz a la cual le asigno el valor que retorne la funcion invocada crear_lista()
    arch_asientos.close() #Cierro el archivo asientos

    cond_eleccion = False
    while not cond_eleccion:
        eleccion = str(input('Elija una asiento (fila:asiento): ')) #Le pido al usuario que ingrese un asiento
        #Este modulo se encarga de sacar el numero de fila del string eleccion
        fila = '' #Creo un string vacio de nombre fila
        for i in eleccion: #Recorro el string eleccion
            if i!=':': #Veo si el caracter del string eleccion es distinto de dos puntos
                fila += i #si es distinto lo sumo al string fila
            else:
                break #Si no es distinto a dos puntos, o sea, es igual a dos puntos salgo abruptamente del loop
        
        #Este modulo se encarga de sacar el numero de asiento del string eleccion
        asiento = '' #Creo un string vacio de nombre asiento
        for i in eleccion[::-1]: #Recorro el string eleccion pero invertido, o sea, del ultimo lugar al primero
            if i!=':': #Veo si el caracter del string eleccion es distinto de dos puntos
                asiento += i #si es distinto lo sumo al string asiento
            else:
                break #Si no es distinto a dos puntos, o sea, es igual a dos puntos salgo abruptamente del loop
        asiento = asiento[::-1] #Invierto el string armado, ya que si lo dejo como lo arme en un principio los valores de este van a estar invertidos
        
        fila = int(fila) #Paso el string fila a una variable de tipo entera
        asiento = int(asiento) #Paso el string asiento a una variable de tipo entera
            
        cond_exist = False #Creo una variable de tipo booleana cond_exist que va a determinar mas adelante si el asiento seleccionado existe
        cond_dispo = False #Creo una variable de tipo booleana cond_dispo que va a determinar mas adelante si el asiento seleccionado esta disponible
        if 0<=fila<=len(matriz) and 0<=asiento<=len(matriz): #Me fijo si la fila y el asiento seleccionado esta dentro de la cantidad de filas y columnas existentes
            cond_exist = True #Si cumple esa condicion significa que el asiento elegido existe, por lo tanto cond_exist lo cambio a True      
            if matriz[fila][asiento]=='0': #Me fijo si el asiento elegido esta disponible indexando la lista de asientos (matriz) en la fila primero y luego en el asiento para que me retorne el valor de ese lugar
                cond_dispo = True #Si el lugar indexado dio 0 significa que esta disponible, por lo tanto cambio la cond_dispo a True
                cond_eleccion = True
            else:
                print('El asiento elegido no esta disponible!') #Si no cumple le avisa al usuario por pantalla
                print('-'*25)
        else:
            print('El asiento elegido no existe!') #Si no cumple le avisa al usuario por pantalla
            print('-'*25)
    
    if cond_exist and cond_dispo: #Verifico que la cond_exist y cond_dispo sean ambas True para continuar. Si no cumple sale del if y termina la funcion venta hasta que el usuario la llame de nuevo
        print('El asiento elegido esta disponible.')
        print('\nPor favor ingrese los siguientes datos...')
            
        cond_dni = False #Creo una condicion cond_dni para ver si el dni ingresado es valido
        while not cond_dni: #Mientras cond_dni sea False el while va a correr
            dni = str(input('DNI: ')) #Le pido al usuario que ingrese su dni
            cond_letra = False #Creo una condicion que me dice si es que en el dni se ingreso alguna letra
            for i in dni: #Para saber si se ingreso alguna letra recorro el string dni
                if es_letra(i): #Veo si alguno de los caracteres es letra
                    cond_letra = True #Si al menos uno es letra cambio la cond_letra a True, dando a entender que hay una letra dentro de dni
                
            if not cond_letra and 7<=len(dni)<=8: #Me fijo si el dni tiene alguna letra y luego si cumple la condicion que debe tener 7 u 8 digitos
                cond_dni = True #Si cumple las condiciones cambio cond_dni a True, dando a entender que el dni ingresado cumple
            else:
                print('\nEl DNI no es valido!') #En cambio di no cumple se le avisa al usuario por pantalla y vuelva a correr el while para preguntarle nuevamente
        
        #Mismo procedimiento que al pedir el dni solo que esta vez pido la edad
        cond_edad = False
        while not cond_edad:
            try: #El try lo puse por si el usuario se equivoca y pone una letra o simbolo en vez de un numero
                edad = int(input('Edad (entre 10 y 110 años): ')) 
                if 10<=edad<=110: #Cambio la condicion de que debe estar entre 10 y 110 años la edad ingresada
                    cond_edad = True
                else:
                    print('\nLa edad tiene que ser mayor a 10 y menor a 110 años!')
            except:
                print('Intente Nuevamente, ocurrio un error. Acuerdese que solo debe ingresar numeros!')
        
        
        #Aca empieza el ingreso del nombre de usuario, buscando que cuando ingrese el nombre de usuario, este no este repetido,
        #o sea, que si la persona, con sierto dni, esta pidiendo el nombre de usuario de otra persona con otro dni, el programa
        #le va a decir que el nombre no esta disponible.
        try: #Trato de abrir el archivo de ventas
            arch_ventas = open('ventas.txt','r') #Primero abro el archivo ventas en modo lectura
            lst_ventas = crear_lista(arch_ventas) #Luego creo una variable de tipo lista llamada lst_ventas que va a tomar el valor que retorne la funcion crear_lista() pasandole por parametro el arch de ventas
        except FileNotFoundError: #Si ve que no existe el archivo crea uno
            arch_ventas = open('ventas.txt','w') 
            arch_ventas.close()
            arch_ventas = open('ventas.txt','r') #Primero abro el archivo ventas en modo lectura
            lst_ventas = crear_lista(arch_ventas) #Luego creo una variable de tipo lista llamada lst_ventas que va a tomar el valor que retorne la funcion crear_lista() pasandole por parametro el arch de ventas
            
        cond_nombre = False #Creo una variable booleana llamada cond_nombre para ver si el dni ingresado es valido 
        if lst_ventas == []: #Primero me fijo si el archivo de ventas esta vacio, o sea, si lst_ventas==[] para saber si es el primer usuario a registrarse
            while not cond_nombre:  #Mientras cond_nombre sea False el while va a correr
                nombre=str(input('Nombre (Al menos 5 letras sin espacios): ')) #Le pido al usuario que ingrese su nombre de usuario
                
                cont_letra = 0
                for i in nombre:
                    if es_letra(i):
                        cont_letra += 1
                    
                if cont_letra>=5 and not(' ' in nombre) and nombre!='': #Verifico que el nombre de usuario tenga minimo 5 caracteres que sean letra, que no tenga espacios en medio y que no sea vacio
                    cond_nombre = True #Si verifica cambia cond_nombre a True, dando a entender que el nombre de usuario ingresado es valido
                else:
                    print('\nEl nombre ingresado no es valido!') #En cambio si no cumple se le avisa al usuario por pantalla y vuelva a correr el while para preguntarle nuevamente
        else: #Si lst_ventas no estaba vacia corre este else        
            lst_nombres = [] #Creo una variable lista vacia llamada lst_nombres en la cual voy a almacenar los nombres de los usuarioa que ya generaron una compra.
            lst_datos = [] #Creo una variable lista vacia llamada lst_datos que va a almacenar la informacion en sublistas de cada nombre de usuario y su respectivo dni
            for i in lst_ventas: #Primero recorro la lista lst_ventas para buscar la informacion de cada compra
                if i[0] not in lst_nombres: #Me fijo que el nombre hayado en la sublista de lst_ventas no este ya en lst_nombre, esto lo hago para que no se repitan nombre de usuarios si es que un mismo usuario compro varias entradas
                    lst_nombres.append(i[0]) #Si verifica agrego el nombre a lst_nombres
            
            ''' Forma de seleccionar los datos sin usar break'''
#             for i in lst_nombres:
#                 j=0
#                 cond = True
#                 while cond and j<len(lst_ventas):
#                     if i == lst_ventas[j][0]:
#                         lst_datos.append([i,lst_ventas[j][1]])
#                         cond = False
#                     j+=1
            
            for i in lst_nombres: #Recorro la lista lst_nombres
                for j in lst_ventas: #Recorro nuevamente la lista lst_ventas para buscar la informacion de cada compra 
                    if i == j[0]: #Me fijo si el nombre seleccionado de lst_nombres es igual al nombre que hay en la sublista j de lst_ventas
                        lst_datos.append([i,j[1]]) #Si verifica le agrego a lst_datos la sublista con el nombre y dni correspondiente
                        break #Invoco a break para salir abruptamente del segundo for y asi no repetir sublistas con los mismos nombre y dni
            
            cond_dni_exist = False #Creo una variable booleana que determine si el dni ingresado ya existia anteriormente o no                
            for i in lst_datos: #Recorro la lista lst_datos 
                if i[1]==dni: #Indexo i, que es una sublista de lst_datos con el nombre y dni de cada usuario, en busca del valor del dni de cada usuario. 
                    #Si ve que el dni ingresado por el usuario es igual al de la indexacion, o sea que ese dni ya habia comprado
                    nombre=i[0] #Primero a la variable nombre le asigna el valor del nombre correspondiente al dni ingresado, el valor de nombre lo saca de lst_datos
                    cond_nombre = True
                    cond_dni_exist = True #Segundo cambia la variable cond_dni_exist a True para dar a entender que ese dni ya existia en la base de datos
                    print('El dni ingresado ya existe y se le asigno el nombre de usuario correspondiente!') #Le aviso al usuario
                    break #Invoco a break para salir abruptamente del for porq ya no es necesario seguir recorriendo lst_datos
            
            while not cond_nombre and not cond_dni_exist: #Si tanto cond_nombre como cond_dni_exist siguen siendo falsos entra al while
                nombre=str(input('Nombre (Al menos 5 letras sin espacios): ')) #Primero le pide que ingrese un nombre de usuario
                cont_letra = 0
                for i in nombre:
                    if es_letra(i):
                        cont_letra += 1
                    
                if cont_letra>=5 and not(' ' in nombre) and nombre!='': #Verifico que el nombre de usuario tenga minimo 5 caracteres que sean letra, que no tenga espacios en medio y que no sea vacio
                    cond_dispo_nombre = True #Si verifica primero creo una variable booleana cond_dispo_nombre que determina si el nombre esta disponible o no, inicialmente asumo que esta disponible
                    for i in lst_datos: #Recorro lst_datos haciendo que la variable i tome el valor de cada sublista de lst_datos
                        if (nombre in i) and (dni not in i): #Me fijo si el nombre de usuario ingresado esta en i y si el dni no esta
                            #Si verifica eso significa que esta queriendo ingresar un nombre de usuario tomado por otro usuario que tiene un dni diferente
                            cond_dispo_nombre = False #Por lo tanto cambio la variable cond_dispo_nombre a False para dar a entender que no esta disponible
                            print('El nombre elegido no esta disponible!') #Le aviso al usuario que el nombre no esta disponible
                            break #invoco break porque ya es innecesario seguir recorriendo lst_datos
                        
                    if cond_dispo_nombre: 
                        cond_nombre = True #Si cond_dispo_nombre sigue siendo True cambio la variable cond_nombre a True tmbn porq significa que el nombre ingresado cumplio todas las condiciones
                else:
                    print('\nEl nombre ingresado no es valido!') #Sino le aviso al usuario que el nombre no es valido
            
        fila_asiento = 'F'+str(fila)+'A'+str(asiento) #Armo el string que contenga la informacion de la fila y asiento con el formato F{}A{}
        
        if fila<len(matriz)/2: #Determino si el asiento elegido es vip o sector general
            precio=20000
        else:
            precio=15000
        
        #Armo el string venta con la informacion que me piden
        str_venta = nombre+','+str(dni)+','+str(edad)+','+fila_asiento+'\n'
        
        arch_ventas = open('ventas.txt','a')#Abro el archivo 'ventas.txt' en el modo 'a' para no sobreescribir el archivo cada vez que
        #almacene informacion nueva en el.
        arch_ventas.write(str_venta) #Le agrego al archivo de ventas el string venta
        arch_ventas.close() #cierro el archivo de ventas
        
        matriz[fila][asiento] = '1'
        guardar_asientos(matriz)
        
        arch_ventas = open('ventas.txt','r') #Abro el archivo ventas de neuvo pero en modo lectura para saber el numero de ticket luego en la funcion gen_ticket
        gen_ticket(nombre,dni,fila_asiento,precio,arch_ventas) #invoco a la funcion gen_ticket
        arch_ventas.close() #cierro el archivo ventas

def gen_ticket(usuario,dni, fila_asiento,precio,arch_ventas):
    #Esta funcion se encarga de generar los tickets
    num_ticket = len(arch_ventas.readlines()) #Aca saco la cantidad de filas que tiene el archivo ventas, esa cantidad me va a decir cuantas ventas ya fueron hechas, o sea, el numero de ticket que tengo que generar
    url_ticket = 'ticket_'+num(num_ticket,4)+'.txt' #Creo el nombre del ticket con el numero de ticket correspondiente
    arch_ticket = open(url_ticket,'w') #Creo el archivo de texto del ticket con el nombre correspondiente
    
    #Le agrego la informacion solicitada al ticket
    arch_ticket.write('Usuario: '+str(usuario)+'\n')
    arch_ticket.write('DNI: '+str(dni)+'\n')
    arch_ticket.write('Asiento: '+str(fila_asiento)+'\n')
    if precio==20000:
        arch_ticket.write('Precio: Sector VIP -'+str(precio)+'\n')
    elif precio==15000:
        arch_ticket.write('Precio: Sector Grl -'+str(precio)+'\n')
    
    arch_ticket.close() #Cierro el archivo del ticket

def buscar_asientos():
    #Esta funcion se va a encargar de buscar un asiento segun el nombre de usuario ingresad. Si el nombre de usuario tiene varios asientos
    #comprados estos se van a ir almacenando en una lista
    arch = open('ventas.txt','r') #abro el archivo 'ventas.txt' en modo lectura ('r')
    lst_ventas = crear_lista(arch) #Creo una variable llamada lst_ventas a la cual le asigno el valor que retorne la funcion invocada crear_lista() pasandole por parametro el arch
    arch.close() #Cierro el archivo
    
    cond = True #Creo una variable booleana llamada cond
    while cond: #Mientras cond sea True el while va a correr
        nombre = str(input('Ingrese su nombre de usuario: ')) #Le pido al usuario que ingrese un nombre de usuario
        lst_asientos = [] #Creo una variable tipo lista vacia llamada lst_asientos la cual va a almacenar los asientos del nombre de usuario seleccionado
        for i in lst_ventas: #Recorro lst_ventas asignandole a i el valor de cada una de sus sublistas
            if nombre in i: #Veo si el nombre ingresado esta dentro de i
                lst_asientos.append(i[3]) #Si esta dentro le agrego a lst_asientos la informacion del asiento en i
                cond = False #Cambio con a False para que no vuelva a correr el while, ya que encontro asientos con el nombre de usuario ingresado
     
    return lst_asientos #Retorno la lista lst_asientos

def buscar_vip():
    #Esta funcion se va a encargar de buscar cuantos usuarios tienen asientos vip
    arch = open('ventas.txt','r') #abro el archivo 'ventas.txt' en modo lectura ('r')
    lst_ventas = crear_lista(arch) #Creo una variable llamada lst_ventas a la cual le asigno el valor que retorne la funcion invocada crear_lista() pasandole por parametro el arch
    arch.close() #Cierro el archivo
    
    lst_vip = [] #Creo una variable de lista vacia llamada lst_vip la cual va a almacenar sublistas con los datos de usuarios con asientos vip ordenados alfabeticamnete
    for i in lst_ventas: #Recorro lst_ventas asignandole a i el valor de cada una de sus sublistas
        str_aux = '' #Creo una variable string vacio llamada str_aux a la cual le voy a agregar el num de fila del asiento seleccionado
        for j in i[3][1:]: #Recorro la sublista i indexada en el elemento que contiene el asiento
            if j!='A': #Recorro el string j hasta que encuentre una 'A'
                str_aux += j #Mientras no encuentre una 'A' le va agregando al str_aux j
            else:
                break #Si encuentra una 'A' invoco a break para salir abruptamente del loop y dejar de agregar valores al str_aux
        
        if int(str_aux) < 24: #Verifico que el numero de fila del asiento cumpla con la condicion para ser vip
            lst_vip.append(i) #Si cumple agrego la sublista i a lst_vip
    
    lst_vip = ordenar(lst_vip) #Por ultimo ordeno lst_vip alfabeticamente por nombre invocando a la funcion ordenar y pasandole por parametro lst_vip
    
    return lst_vip #Retorno lst_vip

def prom_edad():
    arch = open('ventas.txt','r') #abro el archivo 'ventas.txt' en modo lectura ('r')
    lst_ventas = crear_lista(arch) #Creo una variable llamada lst_ventas a la cual le asigno el valor que retorne la funcion invocada crear_lista() pasandole por parametro el arch
    arch.close() #Cierro el archivo
    
    lst_nombres = [] #Creo una variable lista vacia llamada lst_nombres en la cual voy a almacenar los nombres de los usuarioa que ya generaron una compra.    
    for i in lst_ventas: #Primero recorro la lista lst_ventas para buscar la informacion de cada compra
        if i[0] not in lst_nombres: #Me fijo que el nombre hayado en la sublista de lst_ventas no este ya en lst_nombre, esto lo hago para que no se repitan nombre de usuarios si es que un mismo usuario compro varias entradas
            lst_nombres.append(i[0]) #Si verifica agrego el nombre a lst_nombres
    
    #Armo lst_nombres ya que si hay varias entradas compradas por el mismo usario no quiero sumar la edad de este usuario todas las veces
    #que haya comprado, ya que el promedio terminaria dando mal, por lo tanto...        
    
    suma = 0 #Creo una variable de tipo int a la cual le voy a ir sumando las edades
    for i in lst_nombres: #Recorro lst_nombres 
        for j in lst_ventas: #Recorro lst_ventas y le asigno a j el valor de cada sublista de lst_ventas
            if i in j: #Veo si el nombre que selecciono i de lst_nombres esta en la sublista j
                suma += int(j[2]) #Si esta le sumo a la variable suma el dato de edad en la sublista j
                break #Invoco a break ya que no quiero que siga buscando coincidencias en las sublistas de lst_ventas con el mismo nombre, o sea, quiero que cambie el nombre al siguiente en la lista
 
    return suma/len(lst_nombres) #Retorno el promedio de edades 

def recaudacion_total():
    #Esta funcion se va a encargar de ver cual fue la recaudacion total en la venta de entradas
    rec_total = 0 #Creo una variable de tipo int que se llama rec_total
    for i in range(1,2501): #Recorro un rango de 2500 numeros para luego abrir un archivo ticket con el respectivo numero
        url = 'ticket_'+num(i)+'.txt' #Creo una variable de tipo string llamada url la cual va a contener el nombre del archivo ticket a abrir
        try: #Trato de abrir el archivo ticket con tal url
            arch = open(url,'r') #Abre el archivo del ticket con su numero en modo lectura
            lst_arch = arch.readlines() #le asigno a la variable lst_arch una lista donde cada uno de sus elementos es una linea del archivo
            precio = int(lst_arch[len(lst_arch)-1][20:]) #Saco la informacion del precio de lst_arch y los combierto a una variable tipo int
            rec_total += precio #Le sumo el precio hallado a la variable rec_total
            arch.close() #Cierro el archivo
        except FileNotFoundError: #Si no encuentra el archivo sale del loop ya que no hay mas archivos
            break
        
    return rec_total #Retorna la recaudacion total

def menores():
    arch = open('ventas.txt','r') #abro el archivo 'ventas.txt' en modo lectura ('r')
    lst_ventas = crear_lista(arch) #Creo una variable llamada lst_ventas a la cual le asigno el valor que retorne la funcion invocada crear_lista() pasandole por parametro el arch
    arch.close() #Cierro el archivo

    lst_nombres = [] #Creo una variable lista vacia llamada lst_nombres en la cual voy a almacenar los nombres de los usuarioa que ya generaron una compra.    
    for i in lst_ventas: #Primero recorro la lista lst_ventas para buscar la informacion de cada compra
        if i[0] not in lst_nombres: #Me fijo que el nombre hayado en la sublista de lst_ventas no este ya en lst_nombre, esto lo hago para que no se repitan nombre de usuarios si es que un mismo usuario compro varias entradas
            lst_nombres.append(i[0]) #Si verifica agrego el nombre a lst_nombres
    
    lst_usuarios = []
    for i in lst_nombres: #Recorro la lista lst_nombres
        for j in lst_ventas: #Recorro nuevamente la lista lst_ventas para buscar la informacion de cada compra
            if i in j: #Me fijo si el nombre seleccionado de lst_nombres se encuentra en la sublista j de lst_ventas
                if int(j[2])<21: #Verifico que la edad de tal usuario sea menor a 21
                    lst_usuarios.append([i,j[2]]) #Si verifica le agrego a lst_usuarios la sublista con el nombre y edad correspondiente
                break #Invoco a break para salir abruptamente del segundo for y asi no repetir sublistas con los mismos nombre y edad

    lst_usuarios = ordenar(lst_usuarios) #Ordeno alfabeticamente lst_usuarios invocando a la funcion ordenar y pasandole por parametro lst_usuarios
    
    return lst_usuarios #Retorno lst_usuarios

def main():
    while True:
        lst_opciones = [' opcion 01',' opcion 02',' opcion 03',
                        ' opcion 04',' opcion 05',' opcion 06',
                        ' opcion 07',' opcion 08',' opcion 09',
                        ' opcion 10',' opcion 11']
        print('-'*25)
        for i in range(len(lst_opciones)):
            print('-'+lst_opciones[i]+': ' + str(i+1) )
        menu = int(input('Seleccione una opción: '))
        print('-'*25)
        
        #Consigna 1
        if menu==1: #Si elijo el valor 1 printeo la matriz donde se encuentran los datos de cada asiento, si estan ocupados o no.
            print_matriz()
        
        #Consigna 2, 3 y 4
        if menu in (2,3,4): #Si elije 2, 3 o 4 invoca a la funcion venta() y empieza a realizar una venta de un asiento.
            venta()
            print('-'*25)
        
        #Consigna 5
        if menu==5: #Si elije 5 el programa le va a pedir el nombre de usuario para dsps mostrar por pantalla que asientos tiene ese usuario
            lst_asientos = buscar_asientos()
            print(lst_asientos)
            
        #Consigna 6
        if menu==6: #En este caso si elije 6 el programa le va a mostrar a todos los usuarios que hayan comprado un asiento vip ordenados alfabeticamente.
            lst_vip = buscar_vip()
            for i in lst_vip:
                print(i)
        
        #Consigna 7
        if menu==7: #Si elije 7 el programa va a hacer un promedio de edad entre todos los usuarios que hayan comprado.
            prom = prom_edad()
            print(prom)
        
        #Consigna 8
        if menu==8: #Si elije 8 el usuario va a ser capaz de ingresar un numero de ticket para asi poder pedir la informacion de su ticket.
            num_ticket = str(input('Ingrese su numero de ticket: '))
            url = 'ticket_'+num(num_ticket)+'.txt'
            try:
                arch = open(url,'r')
                lst_ticket = arch.readlines()
                
                for i in lst_ticket:
                    print(i,end='')
                    
            except FileNotFoundError:
                print('El numero de ticket ingresado no existe!')
                
        #Consigna 9
        if menu==9: #En el caso de elegir 9 el programa se va a encargar de calcular la recaudación total.
            rec_total = recaudacion_total()
            print(rec_total)
        
        #Consigna 10
        if menu==10: #Si elije 10 el programa le va a retornar una lista con los usuarios que sean menores de 21 años
            lst_menores = menores()
            print(lst_menores)
        
        #Consigna 11
        if menu==11: #Si elige 11 sale del programa.
            break
main()

    
