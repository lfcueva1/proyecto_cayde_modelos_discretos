#libreria que uso para obtener la tecla presionada sin necesidad de presionar Enter
import msvcrt
#libreria que uso para pausar y limpiar pantalla
import os
#libreria que uso para llamar a una funcion que termine el programa
import sys
#libreria que me ayuda con el tiempo de corrida del programa
import time
#libreria que uso para pasar de texto a voz
from gtts import gTTS
def validar_numeros_enteros():
    '''
    Funcion donde se valida si es que el numero ingresado por el usuario es entero, si lo que se ingresó no es un numero
    entero entonces el usuario tendra que volver a ingresar un numero
    Parametros:
    ------------
        Esta funcion no tiene parametros
    Retorna:
    ------------
        numero : int
    '''
    #mientras sea verdadero se ingresara un dato en la variable numero, si lo que se ingreso es un numero entero
    #rompera el ciclo repetitivo while sino el usuario debera volver a ingresar un dato hasta que sea valido
    while True:
        try:
            numero=int(input())
            #rempemos ciclo repetitivo
            break
        except ValueError:
            print("No ha ingresado un numero entero,ingrese de nuevo:",end="")
    return numero
def getch():
    '''
    Funcion que obtiene la tecla presionada sin necesidad de presionar Enter, permitiendo al usuario seleccionar las opciones del 
    menú utilizando las flechas del teclado y presionando Enter para confirmar la selección.
    Parametros:
        Esta funcion no tiene parametros
    Retorna:
        msvcrt.getch()
    '''
    return msvcrt.getch()
def menu_instalaciones_espe():
    '''
    Funcion que imprime un menu de opciones que pregunta al usuario hacia que lugar dentro de la universidad
    de las fuerzas armadas ESPE desea ir el usuario
    Parametros:
        Esta funcion no tiene parametros
    Retorna:
        choice : int
    '''
    #escribo todas las opciones que tendra el menu dentro de una lista
    options = ["1. Entrada( General Rumiñahui)", "2. Parqueadero Espe", "3. Edificio administrativo", "4. Biblioteca", "5. Patio central",
    "6. Canchas de basket","7. Canchas de voley","8. Residencia", "9. Parqueadero residencia", "10. Gimnasio_Coliseo", "11. Estadio de la ESPE",
    "12. Bloque A","13. Bar", "14. Admision y registro","15. Tecnologias de la informacion y comunicacion", "16. Bloque B", "17. Bloque C",
    "18. Bloque D", "19. Bloque H", "20. Bloque G", "21. Laboratorios de biotecnologia", "22. Edificio de centro de investigaciones",
    "23. Entrada(Santa clara)", "24. Laboratorios de fisica","25. Salir"]
    #declarar variable igual a cero
    choice = 0
    #formo un bucle infinito que se encarga de mostrar el menu principal
    while True:
        #limpio pantalla
        os.system("cls")
        print("MENU DE OPCIONES")
        #ciclo repetitivo que permite iterar entre las opcines del menu
        for i, option in enumerate(options):
            if i == choice:
                print("> " + option)
            else:
                print("  " + option)
        #obtiene la tecla presionada por el usuario y se almacena en la variable "key".
        key = getch()
        #verifica si la tecla presionada es "w" y si la opción seleccionada actual es mayor a 0, si es así, la opcion seleccionada se decrementa en 1.
        if key == b"w" and choice > 0:
            choice -= 1
        #verifica si la tecla presionada es "s" y si la opción seleccionada actual es menor al tamaño de las opciones - 1, si es así, la opcion seleccionada se incrementa en 1.
        elif key == b"s" and choice < len(options) - 1:
            choice += 1
        #verifica si la tecla presionada es "Enter" y si es así, se sale del bucle y se devuelve la opcion seleccionada.
        elif key == b"\r":
            return choice

def imprimir_menu():
    '''
    Funcion donde dependiendo de la seleccion del usuario dara valor a una cadena la cual sera enviada
    como parametro en otra funcion

    Parametros:
        Esta funcion no tiene parametros
    Retorna:
        posicion : str
    '''
    posicion=""
    print("Selecciona una opcion:")
    while True:
        opcion = menu_instalaciones_espe()
        if opcion == 0:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=0
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 1:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=1
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 2:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=2
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 3:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=3
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 4:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=4
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 5:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=5
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 6:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=6
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 7:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=7
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 8:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=8
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 9:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=9
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 10:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=10
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 11:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=11
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 12:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=12
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 13:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=13
            #limpio pantalla""
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 14:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=14
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 15:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=15
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 16:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=16
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 17:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=17
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 18:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=18
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 19:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=19
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 20:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=20
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 21:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=21
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 22:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=22
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 23:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            posicion=23
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion==24:
            #si el usuario desea salir a la variable le doy el valor de "25" tipo int para que en el main la detecte y termine el programa
            posicion=24
            #termino el programa
            sys.exit()
    #retorno la cadena
    return posicion

def crear_unir_nodos():
    '''
    Funcion que crea y une a los nodos 
    Parametros:
        
    Retorna:
        Esta funcion no retorna ningun tipo de dato
    '''
    # Crear grafo
    grafo,costo = [[] for i in range(24)],{}
    entrada_general_rumiñahui=0
    parqueadero_espe=1
    edificio_administrativo=2
    biblioteca=3
    patio_central=4
    canchas_de_basket=5
    canchas_de_voley=6
    residencia=7
    parqueadero_residencia=8
    Gimnasio_Coliseo=9
    estadio_de_la_ESPE=10
    bloque_A=11
    bar=12
    admision_y_registro=13
    tecnologias_de_la_informacion_y_comunicacion=14
    bloque_B=15
    bloque_C=16
    bloque_D=17
    bloque_H=18
    bloque_G=19
    laboratorios_de_biotecnologia=20
    edificio_de_centro_de_investigaciones=21
    entrada_santa_clara=22
    laboratorios_de_fisica=23
    #uniendo nodos
    grafo[entrada_general_rumiñahui].append(parqueadero_espe)
    grafo[parqueadero_espe].append(entrada_general_rumiñahui)
    grafo[parqueadero_espe].append(edificio_administrativo)
    grafo[parqueadero_espe].append(residencia)
    grafo[edificio_administrativo].append(biblioteca)
    grafo[edificio_administrativo].append(patio_central)
    grafo[edificio_administrativo].append(canchas_de_voley)
    grafo[biblioteca].append(edificio_administrativo)
    grafo[biblioteca].append(laboratorios_de_fisica)
    grafo[patio_central].append(edificio_administrativo)
    grafo[patio_central].append(canchas_de_basket)
    grafo[patio_central].append(bloque_A)
    grafo[canchas_de_basket].append(patio_central)
    grafo[canchas_de_basket].append(canchas_de_voley)
    grafo[canchas_de_basket].append(estadio_de_la_ESPE)
    grafo[canchas_de_voley].append(edificio_administrativo)
    grafo[canchas_de_voley].append(residencia)
    grafo[canchas_de_voley].append(parqueadero_residencia)
    grafo[canchas_de_voley].append(canchas_de_basket)
    grafo[residencia].append(parqueadero_espe)
    grafo[residencia].append(canchas_de_voley)
    grafo[residencia].append(parqueadero_residencia)
    grafo[parqueadero_residencia].append(canchas_de_voley)
    grafo[parqueadero_residencia].append(residencia)
    grafo[parqueadero_residencia].append(Gimnasio_Coliseo)
    grafo[Gimnasio_Coliseo].append(parqueadero_residencia)
    grafo[Gimnasio_Coliseo].append(edificio_de_centro_de_investigaciones)
    grafo[estadio_de_la_ESPE].append(canchas_de_basket)
    grafo[estadio_de_la_ESPE].append(bar)
    grafo[estadio_de_la_ESPE].append(21)
    grafo[bloque_A].append(patio_central)
    grafo[bloque_A].append(bar)
    grafo[bloque_A].append(admision_y_registro)
    grafo[bloque_A].append(tecnologias_de_la_informacion_y_comunicacion)
    grafo[bloque_A].append(bloque_B)
    grafo[bar].append(estadio_de_la_ESPE)
    grafo[bar].append(bloque_A)
    grafo[admision_y_registro].append(bloque_A)
    grafo[admision_y_registro].append(bloque_B)
    grafo[tecnologias_de_la_informacion_y_comunicacion].append(bloque_A)
    grafo[tecnologias_de_la_informacion_y_comunicacion].append(bloque_B)
    grafo[bloque_B].append(bloque_A)
    grafo[bloque_B].append(admision_y_registro)
    grafo[bloque_B].append(tecnologias_de_la_informacion_y_comunicacion)
    grafo[bloque_B].append(bloque_C)
    grafo[bloque_B].append(bloque_D)
    grafo[bloque_C].append(bloque_B)
    grafo[bloque_C].append(bloque_H)
    grafo[bloque_C].append(laboratorios_de_biotecnologia)
    grafo[bloque_C].append(bloque_D)
    grafo[bloque_C].append(laboratorios_de_fisica)
    grafo[bloque_D].append(bloque_B)
    grafo[bloque_D].append(bloque_C)
    grafo[bloque_D].append(bloque_G)
    grafo[bloque_D].append(laboratorios_de_biotecnologia)
    grafo[bloque_D].append(laboratorios_de_fisica)
    grafo[bloque_H].append(bloque_C)
    grafo[bloque_G].append(bloque_D)
    grafo[laboratorios_de_biotecnologia].append(bloque_C)
    grafo[laboratorios_de_biotecnologia].append(bloque_D)
    grafo[edificio_de_centro_de_investigaciones].append(Gimnasio_Coliseo)
    grafo[edificio_de_centro_de_investigaciones].append(estadio_de_la_ESPE)
    grafo[edificio_de_centro_de_investigaciones].append(entrada_santa_clara)
    grafo[entrada_santa_clara].append(edificio_de_centro_de_investigaciones)
    grafo[laboratorios_de_fisica].append(bloque_D)
    grafo[laboratorios_de_fisica].append(biblioteca)
    return grafo
def busqueda_en_anchura(grafo, costo, inicio, fin):
    '''
    Funcion que busca el camino mas corto en las ubicaciones de la espe

    Parametros:
        grafo : lista
        costo : diccionario
        inicio : int
        fin : int
    Retorna:
        float('inf') : float
        [] : lista
        
    '''
    #variable tipo cola que almacena tupplas con tres elementos: (1) la distancia del nodo 
    #de origen al nodo actual, (2) el nodo actual, y (3) el camino desde el nodo de origen hasta el nodo actual. 
    cola = [(0, inicio, [])]
    #variable que lleva el registro de los nodos que se han visitado durante la búsqueda.
    visitados = set()
    #recorremos la cola mientras no este vacia
    while cola:
        #Se toma el primer elemento de la cola (el nodo con la distancia mínima hasta ese momento)
        (dist, actual, camino) = cola.pop(0)
        #Si el nodo actual es el nodo de destino fin
        if actual == fin:
            #se devuelve la distancia total y el camino desde el nodo de origen hasta el nodo de destino.
            return dist, camino + [actual]
        #Si el nodo actual ha sido visitado previamente
        if actual in visitados:
            #se omite este nodo y se continúa con el siguiente.
            continue
        #Se agrega el nodo actual al conjunto de nodos visitados.
        visitados.add(actual)
        #Se recorre sobre los vecinos del nodo actual.
        for vecino in grafo[actual]:
            #Se obtiene el costo para llegar desde el nodo actual hasta su vecino, o se asigna un costo predeterminado 
            #de 1 si no se encuentra en el diccionario costo.
            costo_vecino = costo.get((actual, vecino), 1)
            #Se agrega una nueva tupla a la cola con la nueva distancia total, el vecino y el camino actualizado 
            # (agregando el nodo actual al camino).
            cola.append((dist + costo_vecino, vecino, camino + [actual]))
    #Si no se encuentra un camino desde el nodo de origen hasta el nodo de destino, se devuelve una distancia infinita y un camino vacío.
    return float('inf'), []

def ubicaciones(voz_camino):
    '''
    Funcion que de el nombre de una ubicacion a una lista segun el valor que tenga

    Parametros:
        voz_camino : lista
    Retorna: 
        voz_camino : lista
    '''
    #recorremos la lista entera y damos el nombre de la ubicacion dependiendo el numero que tenga el nodo
    for i in camino:
        if(i==0):
            voz_camino.append("Entrada general rumiñaui")
        if(i==1):
            voz_camino.append("Parqueadero Espe")
        if(i==2):
            voz_camino.append("Edificio administrativo")
        if(i==3):
            voz_camino.append("Biblioteca")
        if(i==4):
            voz_camino.append("Patio central")
        if(i==5):
            voz_camino.append("Canchas de basket")
        if(i==6):
            voz_camino.append("Canchas de voley")
        if(i==7):
            voz_camino.append("Residencia")    
        if(i==8):
            voz_camino.append("Parqueadero residencia")
        if(i==9):
            voz_camino.append("Gimnasio_Coliseo")   
        if(i==10):
            voz_camino.append("Estadio de la ESPE") 
        if(i==11):
            voz_camino.append("Bloque A") 
        if(i==12):
            voz_camino.append("Bar")  
        if(i==13):
            voz_camino.append("Admision y registro") 
        if(i==14):
            voz_camino.append("Tecnologías de la información") 
        if(i==15):
            voz_camino.append("Bloque B") 
        if(i==16):
            voz_camino.append("Bloque C") 
        if(i==17):
            voz_camino.append("Bloque D") 
        if(i==18):
            voz_camino.append("Bloque H") 
        if(i==19):
            voz_camino.append("Bloque G") 
        if(i==20):
            voz_camino.append("Laboratorios de biotecnologias")
        if(i==21):
            voz_camino.append("Edificio de investigacion")   
        if(i==22):
            voz_camino.append("Entrada Santa Clara") 
        if(i==23):
            voz_camino.append("Laboratorios de fisica") 
    #retornamos el camino
    return voz_camino
if __name__ == '__main__':
    #creo y uno los nodos
    grafo=crear_unir_nodos()
    #limpio pantalla
    os.system("cls")
    #Frase que dira la IA al comenzar el programa
    texto="Bienvenido, sere tu guian para que puedas movilizarte a traves de la universidad de las fuerzas armadas ESPE, dime, en donde te encuentras?"
    #selecciono el lenguaje
    language="es-us"
    #guardo los parametros
    speech = gTTS(text=texto, lang=language,slow=False)
    #guardamos el mp3
    speech.save("texto.mp3")
    #hacemos que la IA hable por parlantes
    os.system("start texto.mp3")
    time.sleep(8)
    while True:
        #imprimo el menu donde inserto mi posicion inicial y elijo una de las opciones
        print("\033[1;32m"+"")#color verde
        punto_inicio=imprimir_menu()
        #limpio pantalla
        os.system("cls")
        print("\033[1;34m"+"")#color cian
        #Agente inteligente pregunta a donde quieres ir
        texto="A que lugar de la espe te gustaría ir?"
        #selecciono el lenguaje
        language="es-us"
        #guardo los parametros
        speech = gTTS(text=texto, lang=language,slow=False)
        #guardamos el mp3
        speech.save("texto.mp3")
        #hacemos que la IA hable por parlantes
        os.system("start texto.mp3")
        #imprimo el menu2 donde inserto mi posicion final(hacia donde el usuario quiere ir) y elijo una de las opciones
        punto_final=imprimir_menu()
        #declaro un diccionario para calcular el costo
        costo = {}
        #busco el camino mas corto para llegar a la ubicacion deseada y caluclo el costo
        costo_1,camino=busqueda_en_anchura(grafo, costo, punto_inicio, punto_final)
        #declaro una lista vacia la cual usare para agregar las ubicaciones por donde el usuario tendra que pasar para llegar a su destino
        voz_camino=[]
        #agrego los caminos a la lista
        voz_camino=ubicaciones(voz_camino)
        #imprimo el camino mas corto y el valor del costo

        #texto que dira por parlantes el agente inteligente
        texto="Para llegar a tu destino sigue el siguiente camino: {0}, el costo sera de {1}".format(voz_camino,costo_1)
        #selecciono el lenguaje
        language="es-us"
        #guardo los parametros
        speech = gTTS(text=texto, lang=language,slow=False)
        #guardamos el mp3
        speech.save("texto.mp3")
        #hacemos que la IA hable por parlantes
        os.system("start texto.mp3")
        print("El costo es: ",costo_1)
        print("El camino que debes tomar es:", voz_camino)
        
        #texto que dira por parlantes el agente inteligente
        os.system("pause")
        print("Deseas continuar con el programa?\n1:Si\n2:No")
        print("Elije una opcion: ",end="")
        texto="Necesitas algo mas? Ingrese 1 para si ó ingrese 2 para no"
        #selecciono el lenguaje
        language="es-us"
        #guardo los parametros
        speech = gTTS(text=texto, lang=language,slow=False)
        #guardamos el mp3
        speech.save("texto.mp3")
        #hacemos que la IA hable por parlantes
        os.system("start texto.mp3")
        #ingreso si quiero continuar el programa o terminarlo
        continuar=validar_numeros_enteros()
        #valido el rango del menu
        while(continuar<1 or continuar>2):
            #texto que dira por parlantes el agente inteligente
            texto="Lo que ingreso no se encuentra dentro del menu, intente de nuevo"
            #selecciono el lenguaje
            language="es-us"
            #guardo los parametros
            speech = gTTS(text=texto, lang=language,slow=False)
            #guardamos el mp3
            speech.save("texto.mp3")
            #hacemos que la IA hable por parlantes
            os.system("start texto.mp3")
            print("Ingrese un numero valido: ",end="")
            continuar=validar_numeros_enteros()
        if(continuar==2):
            #texto que dira por parlantes el agente inteligente
            texto="Fue un gusto haberte ayudado, hasta la proxima"
            #selecciono el lenguaje
            language="es-us"
            #guardo los parametros
            speech = gTTS(text=texto, lang=language,slow=False)
            #guardamos el mp3
            speech.save("texto.mp3")
            #hacemos que la IA hable por parlantes
            os.system("start texto.mp3")
            sys.exit()