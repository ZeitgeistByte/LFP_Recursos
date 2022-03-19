from Analizador import AnalizadorLexico
from AnalizadorSintactico import AnalizadorSintactico

cadena = open('./AFDejemplo2/entrada.txt','r+').read()

#Instancia de analizador lexico
lexico = AnalizadorLexico()


lexico.analizar(cadena)

#lexico.imprimirTokens()

#Guardar lista de tokens
listaTokens = lexico.listaTokens




#Implementar mi analizador sintáctico
sintactico = AnalizadorSintactico(listaTokens)
print(len(listaTokens))

sintactico.analizar()

print(sintactico.errores)

# # identificador igual numero puntoycoma
# #   i            i+1    i+2   i+3
# variables = {}



# def obtenerValor(token,diccionario):
#     if token.tipo == 'numero':
#         return int(token.lexema)
#     elif token.tipo == 'identificador':
#         return diccionario[token.lexema]


# for i in range(0,len(listaTokens)):
#     if listaTokens[i].tipo == 'signoIgual':
#         variables[listaTokens[i-1].lexema] = int(listaTokens[i+1].lexema)
#     # reservada_restar parIzq numero|identificador coma numero|identificador parDer puntoyComa
#     #   i                i+1   i+2                  i+3     i+4               i+5      i+6
#     if listaTokens[i].tipo == 'reservada_restar':
#         num1 = obtenerValor(listaTokens[i+2],variables)
#         num2 = obtenerValor(listaTokens[i+4],variables)
#         print("Resta",num1-num2)

#     if listaTokens[i].tipo == 'reservada_sumar':
#         num1 = obtenerValor(listaTokens[i+2],variables)
#         num2 = obtenerValor(listaTokens[i+4],variables)
#         print("Suma",num1+num2)

#     if listaTokens[i].tipo == 'reservada_dividir':
#         num1 = obtenerValor(listaTokens[i+2],variables)
#         num2 = obtenerValor(listaTokens[i+4],variables)
#         print("División",num1/num2)

#     if listaTokens[i].tipo == 'reservada_multiplicar':
#         num1 = obtenerValor(listaTokens[i+2],variables)
#         num2 = obtenerValor(listaTokens[i+4],variables)
#         print("Multiplicación",num1*num2)