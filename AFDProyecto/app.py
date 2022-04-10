import enum
from Analizador import AnalizadorLexico
from creadorHTML import crearHTML

cadena = open('./AFDProyecto/entrada.txt','r+').read()

#Instancia de analizador lexico
lexico = AnalizadorLexico()


lexico.analizar(cadena)

#lexico.imprimirTokens()

#Guardar lista de tokens
listaTokens = lexico.listaTokens
lexico.imprimirTokens()
lexico.imprimirErrores()

#Creación de archivo html
crearHTML(listaTokens)