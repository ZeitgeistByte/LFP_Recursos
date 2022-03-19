'''
INICIO ::= ASIGNACIONES

ASIGNACIONES ::= ASIGNACION ASIGNACIONES2

ASIGNACIONES2 ::= ASIGNACION ASIGNACIONES2
ASIGNACIONES2 ::= epsilon

ASIGNACION ::= identificador signoIgual numero puntoYComa

'''


class AnalizadorSintactico:

    def __init__(self,tokens : list) -> None:
        self.errores = []
        self.tokens = tokens
        self.tokens.reverse()
        self.diccionario = {}

    def agregarError(self,esperado,token):
        self.errores.append(
            '''ERROR SINTÁCTICO: se obtuvo {} se esperaba {}'''.format(token.tipo,esperado)
        )

    def analizar(self):
        try:
            self.INICIO()
        except:
            pass
    def INICIO(self):
        self.ASIGNACIONES()

    def ASIGNACIONES(self):
        self.ASIGNACION()
        self.ASIGNACIONES2()

    def ASIGNACION(self):
        nombre_variable = ''
        valor = 0
        token = self.tokens.pop()
        if token.tipo == 'identificador':
            nombre_variable = token.lexema
            token = self.tokens.pop()
            if token.tipo == 'signoIgual':
                token = self.tokens.pop()
                if token.tipo == 'numero':
                    valor = int(token.lexema)
                    token = self.tokens.pop()
                    if token.tipo == 'puntoYComa':
                        self.diccionario[nombre_variable] = valor
                        print(self.diccionario)
                    else:
                        #error se esperaba puntoYComa
                        self.agregarError('puntoYComa',token)
                else:
                    #error se esperaba numero
                    self.agregarError('numero',token)
            else:
                #error se esperaba signoIgual
                self.agregarError('signoIgual',token)
        else:
            #error se esperaba identificador
            self.agregarError('identificador',token)

    def ASIGNACIONES2(self):
        token = self.tokens[-1]
        if token.tipo == 'identificador':
            self.ASIGNACION()
            self.ASIGNACIONES2()
        else:
            pass

