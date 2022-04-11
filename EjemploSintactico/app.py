from Analizador import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico


while True:
    lexico = AnalizadorLexico()

    cadena = input("Ingrese comando: ")

    lexico.analizar(cadena)

    #Guardar lista de tokens
    listaTokens = lexico.listaTokens

    #Análisis sintáctico
    sintactico = AnalizadorSintactico(listaTokens)
    sintactico.analizar()
    sintactico.imprimirErrores()

