#libreria que uso para la creacion y union de nodos
import networkx as nx
#libreria que uso para obtener la tecla presionada sin necesidad de presionar Enter
import msvcrt
#libreria que uso para pausar y limpiar pantalla
import os
#libreria que uso para llamar a una funcion que termine el programa
import sys
#libreria que uso para abrir y cerrar imagenes
import cv2
#libreria que uso para pasar de texto a voz
from gtts import gTTS

import time
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
    "6. Canchas de basket","7. Canchas de voley","8. Residencia", "9. Parqueadero residencia", "10. Gimnasio", "11. Estadio de la ESPE",
    "12. Bloque A","13. Bar", "14. Admision y registro","15. Tecnologias de la informacion y comunicacion", "16. Bloque B", "17. Bloque C",
    "18. Bloque D", "19. Bloque H", "20. Bloque G", "21. Laboratorios de biotecnologia", "22. Edificio de centro de investigaciones",
    "23. Entrada(Santa clara)", "24. Laboratorios de fisica", "25. Salir"]
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
def calcular_costo(camino):
    '''
    Funcion que calcula el costo

    Parametros:
        camino : lista
    '''
    # Calcular costo
    costo = 0
    for i in range(len(camino) - 1):
        costo += 1
    print("El costo total es:", costo)
def mapa_espe(punto_de_inicio,punto_final):
    '''
    Funcion que crea y une a los nodos 
    Parametros:
        punto_de_inicio :  str
        punto_final : str
    Retorna:
        Esta funcion no retorna ningun tipo de dato
    '''

    # Crear grafo
    G = nx.Graph()
    G.add_node("Entrada( General Rumiñahui)")
    G.add_node("Parqueadero Espe")
    G.add_node("Edificio administrativo")
    G.add_node("Biblioteca")
    G.add_node("Patio central")
    G.add_node("Canchas de basket")
    G.add_node("Canchas de voley")
    G.add_node("Residencia")
    G.add_node("Parqueadero residencia")
    G.add_node("Gimnasio")
    G.add_node("Estadio de la ESPE")
    G.add_node("Bloque A")
    G.add_node("Bar")
    G.add_node("Admision y registro")
    G.add_node("Tecnologias de la informacion y comunicacion")
    G.add_node("Bloque B")
    G.add_node("Bloque C")
    G.add_node("Bloque D")
    G.add_node("Bloque H")
    G.add_node("Bloque G")
    G.add_node("Laboratorios de biotecnologia")
    G.add_node("Edificio de centro de investigaciones")
    G.add_node("Entrada(Santa clara)")
    G.add_node("Laboratorios de fisica")
    #uniendo los nodos
    G.add_edge("Entrada( General Rumiñahui)", "Parqueadero Espe")#1
    G.add_edge("Parqueadero Espe", "Edificio administrativo")#2
    G.add_edge("Parqueadero Espe", "Residencia")#2
    G.add_edge("Edificio administrativo", "Biblioteca")#3
    G.add_edge("Edificio administrativo","Patio central")#3
    G.add_edge("Edificio administrativo","Canchas de voley")#3
    G.add_edge("Biblioteca", "Laboratorios de fisica")#4
    G.add_edge("Patio central", "Canchas de basket")#5
    G.add_edge("Patio central","Bloque A")#5
    G.add_edge("Canchas de basket", "Canchas de voley")#6
    G.add_edge("Canchas de basket", "Estadio de la ESPE")#6
    G.add_edge("Canchas de voley", "Residencia")#7
    G.add_edge("Canchas de voley", "Parqueadero residencia")#7
    G.add_edge("Residencia", "Parqueadero residencia")#8
    G.add_edge("Parqueadero residencia", "Gimnasio")#9
    G.add_edge("Gimnasio", "Edificio de centro de investigaciones")#10
    G.add_edge("Estadio de la ESPE", "Bar")#11
    G.add_edge("Estadio de la ESPE", "Edificio de centro de investigaciones")#11
    G.add_edge("Bloque A", "Bar")#12
    G.add_edge("Bloque A", "Admision y registro")#12
    G.add_edge("Bloque A", "Tecnologias de la informacion y comunicacion")#12
    G.add_edge("Bloque A", "Bloque B")#12
    #G.add_edge("Bar", "Estadio de la ESPE", "Bloque A")#13
    G.add_edge("Admision y registro", "Bloque B")#14
    G.add_edge("Tecnologias de la informacion y comunicacion", "Bloque B")#15
    G.add_edge("Bloque B", "Bloque C")#16
    G.add_edge("Bloque B", "Bloque D")#16
    G.add_edge("Bloque C", "Bloque D")#17
    G.add_edge("Bloque C", "Bloque H")#17
    G.add_edge("Bloque C", "Laboratorios de biotecnologia")#17
    G.add_edge("Bloque C", "Laboratorios de fisica")#17
    G.add_edge("Bloque D", "Bloque G")#18
    G.add_edge("Bloque D", "Laboratorios de biotecnologia")#18
    G.add_edge("Bloque D", "Laboratorios de fisica")#18
    #G.add_edge("Bloque H", "Bloque C")#19
    #G.add_edge("Bloque G", "Bloque D")#20
    #G.add_edge("Laboratorios de biotecnologia", "Bloque C", "Bloque D")#21
    G.add_edge("Edificio de centro de investigaciones", "Entrada(Santa clara)")#22
    #G.add_edge("Entrada(Santa clara)", "Edificio de centro de investigaciones")#23
    #G.add_edge("Laboratorios de fisica", "Biblioteca", "Bloque C", "Bloque D")#24
    # Encontrar camino más rápido para llegar de un  punto a otro
    camino = nx.shortest_path(G, punto_de_inicio,punto_final)
    print("El camino más rápido desde ",punto_de_inicio, "a ",punto_final," es:", camino)
    #Frase que dira la IA al comenzar el programa
    texto="El camino más rápido desde {0} hasta {1} es {2}".format(punto_de_inicio,punto_final,camino)
    #selecciono el lenguaje
    language="es-us"
    #guardo los parametros
    speech = gTTS(text=texto, lang=language,slow=False)
    #guardamos el mp3
    speech.save("texto.mp3")
    #hacemos que la IA hable por parlantes
    os.system("start texto.mp3")
    
    calcular_costo(camino)
def imprimir_menu():
    '''
    Funcion donde dependiendo de la seleccion del usuario dara valor a una cadena la cual sera enviada
    como parametro en otra funcion

    Parametros:
        Esta funcion no tiene parametros
    Retorna:
        punto_de_partida : str
    '''
    punto_de_partida=""
    print("Selecciona una opcion:")
    while True:
        opcion = menu_instalaciones_espe()
        if opcion == 0:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Entrada( General Rumiñahui)"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 1:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Parqueadero Espe"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 2:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Edificio administrativo"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 3:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Biblioteca"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 4:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Patio central"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 5:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Canchas de basket"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 6:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Canchas de voley"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 7:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Residencia"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 8:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Parqueadero residencia"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 9:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Gimnasio"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 10:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Estadio de la ESPE"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 11:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Bloque A"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 12:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Bar"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 13:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Admision y registro"
            #limpio pantalla""
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 14:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Tecnologias de la informacion y comunicacion"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 15:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Bloque B"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 16:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Bloque C"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 17:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Bloque D"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 18:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Bloque H"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 19:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Bloque G"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 20:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Laboratorios de biotecnologia"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 21:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Edificio de centro de investigaciones"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 22:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Entrada(Santa clara)"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion == 23:
            #Doy el nombre del lugar donde se encuentra el usuario actualmente
            punto_de_partida="Laboratorios de fisica"
            #limpio pantalla
            os.system("cls")
            #rompo ciclo reptitivo
            break
        if opcion==24:
            #si el usuario desea salir a la variable le doy el valor de "salir" tipo str para que en el main la detecte y termine el programa
            punto_de_partida="Salir"
            #rompo ciclo reptitivo
            break
    #retorno la cadena
    return punto_de_partida

#funcion main
if __name__ == '__main__': 

    #Frase que dira la IA al comenzar el programa
    texto="Hola, mi nombre es Cayd, durante el uso de este programa sere tu guía para llevarte a cualquier lugar de la universidad de las Fuerzas armadas espe, para continuar presione cualquier tecla"
    #selecciono el lenguaje
    language="es-us"
    #guardo los parametros
    speech = gTTS(text=texto, lang=language,slow=False)
    #guardamos el mp3
    speech.save("texto.mp3")
    #hacemos que la IA hable por parlantes
    os.system("start texto.mp3")
    time.sleep(1)
    # Cargar imagen
    img = cv2.imread("clovis.jpg")
    # Mostrar imagen
    cv2.imshow("Cayde", img)
    # Esperar a que se presione una tecla
    cv2.waitKey(0)
    # Cerrar ventana
    cv2.destroyAllWindows()
    #creo un ciclo repetitivo para que mi agente inteligente siga funcionando una halla cumplido su objetivo
    while True:
        #limpio pantalla
        os.system("cls")
        #Frase que dira la IA al comenzar el programa
        texto="Ingrese en que parte de la ESPE se encuentra en este momento"
        #selecciono el lenguaje
        language="es-us"
        #guardo los parametros
        speech = gTTS(text=texto, lang=language,slow=False)
        #guardamos el mp3
        speech.save("texto.mp3")
        #hacemos que la IA hable por parlantes
        os.system("start texto.mp3")
        #imprimo el menu donde inserto mi posicion inicial y elijo una de las opciones
        print("\033[1;32m"+"")#color verde
        #pauso codigo 
        #os.system("pause")
        punto_de_inicio=imprimir_menu()
        #si ha elegido la opcion  de sallir el programa terminara
        if(punto_de_inicio=="Salir"):
            #termino el programa
            sys.exit()
        
        #Frase que dira la IA al comenzar el programa
        texto="Ingrese a que parte de la ESPE desea ir"
        #selecciono el lenguaje
        language="es-us"

        #guardo los parametros
        speech = gTTS(text=texto, lang=language,slow=False)
        #guardamos el mp3
        speech.save("texto.mp3")
        #hacemos que la IA hable por parlantes
        os.system("start texto.mp3")
        #imprimo el menu donde inserto la posicion hacia donde quiero ir y elijo una de las opciones
        print("\033[1;34m"+"")#color cian
        #pauso codigo 
        #os.system("pause")
        punto_final=imprimir_menu()
        #si ha elegido la opcion  de sallir el programa terminara
        if(punto_final=="Salir"):
            #termino el programa
            sys.exit()
        if(punto_de_inicio==punto_final):
            #Frase que dira la IA al comenzar el programa
            texto="Usted ya se encuentra en esa posicion"
            #selecciono el lenguaje
            language="es-us"
            #guardo los parametros
            speech = gTTS(text=texto, lang=language,slow=False)
            #guardamos el mp3
            speech.save("texto.mp3")
            #hacemos que la IA hable por parlantes
            os.system("start texto.mp3")
        else:
            #imprimo el camino que deberia tomar el usuario para llegar al punto donde desea ir
            mapa_espe(punto_de_inicio,punto_final)
        #pauso el programa
        os.system("pause")
        #Frase que dira la IA al comenzar el programa
        texto="Deseas ir a otro lugar?"
        #selecciono el lenguaje
        language="es-us"
        #guardo los parametros
        speech = gTTS(text=texto, lang=language,slow=False)
        #guardamos el mp3
        speech.save("texto.mp3")
        #hacemos que la IA hable por parlantes
        os.system("start texto.mp3")
        print("Elija una opcion")
        print("1: Si\n2: No")
        opcion_ciclo_repetitivo=validar_numeros_enteros()
        while(opcion_ciclo_repetitivo<1 or opcion_ciclo_repetitivo>2):
            print("Ingrese solo numeros dentro del rango: ")
            opcion_ciclo_repetitivo=validar_numeros_enteros()
        if(opcion_ciclo_repetitivo==2):
            #Frase que dira la IA al comenzar el programa
            texto="Fue un gusto haberte ayudado, adios"
            #selecciono el lenguaje
            language="es-us"
            #guardo los parametros
            speech = gTTS(text=texto, lang=language,slow=False)
            #guardamos el mp3
            speech.save("texto.mp3")
            #hacemos que la IA hable por parlantes
            os.system("start texto.mp3")
            break
