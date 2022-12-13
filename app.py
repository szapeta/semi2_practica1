import pyodbc
import pandas as pd
import config
import logging

#Configurar nuestro log
logger = logging.getLogger('Practica1')
logger.setLevel(logging.DEBUG)
ch = logging.FileHandler('logs.log', 'w',encoding = 'UTF-8')
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

def main():
    archivo=open('resultados.txt','w',encoding="utf-8")
    archivo.close()
    menu()

def menu():
    crear_modelo = '1'
    cargar_informacion = '2'
    realizar_consultas = 3
    salir = 4
    while True:
        print('********* Elije una opción *********')
        print('1. Crear modelo')
        print('2. Cargar informacion')
        print('3. Realizar consultas')
        print('4. Salir')
        print('************************************')
        print("")
        print("")
        print("")
        
        opcion = input('Seleccione una opcion: ')
        if opcion== crear_modelo:
            logger.info("Usuario selecciona opcion de creacion de modelo")
            creacion()
        elif opcion== cargar_informacion:
            logger.info('Usuario selecciona opcion de ejecutar consultas')
            creacion()
        elif opcion== realizar_consultas:
            logger.info('Usuario selecciona opcion de ejecutar consultas')
            creacion()
        else:
            #conn.close()
            logger.info('Conexion finalizada')
            exit()

def creacion():
    print("Creando...")

if __name__ == "__main__":
    main()
    logger.info('Aplicacion finalizada')
