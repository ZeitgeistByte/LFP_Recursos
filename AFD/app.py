from Analizador import AnalizadorLexico


#Ya no es necesario que agreguen un caracter extra al final
cadena = 'abbaaaaabbabb bbbbaaaaaaaaabb'

#Instancia de analizador lexico
lexico = AnalizadorLexico()


lexico.analizar(cadena)
lexico.imprimirTokens()
lexico.imprimirErrores()