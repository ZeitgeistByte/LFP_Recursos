from Token import Token
from Error import Error
from prettytable import PrettyTable

class AnalizadorLexico:
    
    def __init__(self) -> None:
        self.listaTokens  = []
        self.listaErrores = []
        self.linea = 1
        self.columna = 0
        self.buffer = ''
        self.estado = 1
        self.i = 0

    def q1(self,caracter):
        '''Estado q1'''
        if caracter == 'a':
            self.buffer += caracter
            self.columna += 1
            self.estado = 2
        elif caracter == 'b':
            self.buffer += caracter
            self.columna += 1
            self.estado = 1
        else:
            #Error
            self.listaErrores.append(
                Error("ERROR caracter  {} desconocido".format(caracter),
                self.linea,
                self.columna))

    def q2(self,caracter):
        ''' Estado q2'''
        if caracter == 'a' or caracter == 'A':
            self.buffer += caracter
            self.columna += 1
            self.estado = 2
        elif caracter == 'b':
            self.buffer += caracter
            self.columna += 1
            self.estado = 3     
        else:
            #Error
            self.listaErrores.append(
                Error("ERROR caracter  {} desconocido".format(caracter),
                self.linea,
                self.columna))  
            self.estado = 1     
            self.buffer = ''      

    def q3(self,caracter):
        ''' Estado q3 '''
        if caracter == 'a':
            self.buffer += caracter
            self.columna += 1
            self.estado = 2
        elif caracter == 'b':
            self.buffer += caracter
            self.columna += 1
            self.estado = 4     
        else:
            #Error
            self.listaErrores.append(
                Error("ERROR caracter  {} desconocido".format(caracter),
                self.linea,
                self.columna))  
            self.estado = 1     
            self.buffer = ''         

    def q4(self,caracter):
        ''' Estado q4 '''
        if caracter == 'a':
            self.buffer += caracter
            self.columna += 1
            self.estado = 2
        elif caracter == 'b':
            self.buffer += caracter
            self.columna += 1
            self.estado = 1     
        else:
            #Agregar token
            self.listaTokens.append(
                    Token(self.buffer,
                        self.linea,
                        self.columna,
                        'TOKEN DE AB'))
            #Error
            self.listaErrores.append(
                Error("ERROR caracter  {} desconocido".format(caracter),
                self.linea,
                self.columna))  
            self.estado = 1     
            self.buffer = ''   

    def analizar(self, cadena):
        '''Maneja el cambio de estados'''
        cadena += '$'
        self.listaErrores = []
        self.listaTokens = []

        self.i = 0

        while self.i < len(cadena):
            if self.estado == 1:
                self.q1(cadena[self.i])
            elif self.estado == 2:
                self.q2(cadena[self.i])
            elif self.estado == 3:
                self.q3(cadena[self.i])
            elif self.estado == 4:
                self.q4(cadena[self.i])
            self.i += 1    

    def imprimirTokens(self):
        '''Imprime una tabla con los tokens'''
        x = PrettyTable()
        x.field_names = ["Lexema","linea","columna","tipo"]
        for token in self.listaTokens:
            x.add_row([token.lexema, token.linea, token.columna,token.tipo])
        print(x)

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["DEscripcion","linea","columna"]
        for error_ in self.listaErrores:
            x.add_row([error_.descripcion, error_.linea, error_.columna])
        print(x)        