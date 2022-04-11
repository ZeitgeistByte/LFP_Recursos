from ast import Pass
import json

from prettytable import PrettyTable
def createDB(nombre):
    cadena = ''
    with open("bases.txt",'r+') as file:
        diccionario = json.loads(file.read())
        diccionario["bases"][nombre] = {}
        cadena = json.dumps(diccionario)
    escribir(cadena)
    print("Se creó base de datos",nombre)

def createTable(nombre,base):
    cadena = ''
    with open("bases.txt",'r+') as file:
        diccionario = json.loads(file.read())
        diccionario["bases"][base][nombre] = []
        cadena = json.dumps(diccionario)
    escribir(cadena)
    print("Se creó en la base de datos",base,"la tabla",nombre)

def insertar(tabla,base,registro):
    cadena = ''
    with open("bases.txt",'r+') as file:
        diccionario = json.loads(file.read())
        diccionario["bases"][base][tabla].append(list(registro))
        cadena = json.dumps(diccionario)
    escribir(cadena)
    print("Se insertó en la tabla",tabla,"de la base",base,"un registro")

def escribir(cadena):
    with open("bases.txt",'w') as file:
        file.write(cadena)

def imprimir(tabla,base):
    print("Imprimiendo tabla",tabla,"de la base",base)
    lista = []
    with open("bases.txt",'r') as file:
        lista = json.loads(file.read())["bases"][base][tabla]
    x = PrettyTable()
    for registro in lista:
        x.add_row(registro)
    print(x)        
