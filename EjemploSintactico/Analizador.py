from soupsieve import select
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
        self.estado = 0
        self.simbolo = ''
        self.i = 0

    def agregar_token(self,caracter,linea,columna,token):
        self.listaTokens.append(Token(caracter,linea,columna,token))
        self.buffer = ''


    def agregar_error(self,caracter,linea,columna):
        self.listaErrores.append(Error('Lexema ' + caracter + ' no reconocido en el lenguaje.', linea, columna))
        self.buffer = ''

    def s0(self,caracter : str):
        '''Estado S0'''
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1      
        elif caracter.isdigit():
            self.estado = 4
            self.buffer += caracter
            self.columna += 1               
        elif caracter == '\"':
            self.estado = 2
            self.buffer += caracter
            self.columna += 1     
        elif caracter == '.':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
            self.simbolo = 'punto'
        elif caracter == '(':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
            self.simbolo = 'parentesisIzquierdo'
        elif caracter == ')':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
            self.simbolo = 'parentesisDerecho'                        
        elif caracter == ',':
            self.estado = 6
            self.buffer += caracter
            self.columna += 1
            self.simbolo = 'coma'
        elif caracter== '\n':
            self.linea += 1
            self.columna = 0
        elif caracter in ['\t',' ']:
            self.columna += 1
        elif caracter == '$':
            pass
        else:
            self.agregar_error(caracter,self.linea,self.columna)
            self.columna += 1
            self.estado = 0

    def s1(self,caracter : str):
        '''Estado S1'''
        if caracter.isalpha():
            self.estado = 1
            self.buffer += caracter
            self.columna += 1                                               
        else: 
            if self.buffer in ['CREAR','BASE','EN','TABLA','INSERTAR','IMPRIMIR']:
                self.agregar_token(self.buffer,self.linea,self.columna,'reservada_'+self.buffer)    
                self.estado = 0
                self.i -= 1
            else:
                self.agregar_error(self.buffer,self.linea,self.columna)
                self.columna += 1
                self.estado = 0
                self.i -= 1

             

    def s2(self,caracter : str):
        '''Estado S2'''
        if caracter == '"':
            self.estado = 3
            self.buffer += caracter
            self.columna += 1
        else:
            self.buffer += caracter
            self.columna += 1

    def s3(self,caracter : str):
        '''Estado S3'''
        self.agregar_token(self.buffer,self.linea,self.columna,'cadena')
        self.estado = 0
        self.i -= 1

    def s4(self,caracter : str):
        '''Estado S1'''
        if caracter.isdigit():
            self.estado = 4
            self.buffer += caracter
            self.columna += 1                                               
        else: 
            self.agregar_token(self.buffer,self.linea,self.columna,'entero')    
            self.estado = 0
            self.i -= 1  

    def s6(self,caracter : str):
        '''Estado S6'''
        self.agregar_token(self.buffer,self.linea,self.columna,self.simbolo)
        self.estado = 0
        self.i -= 1

    def analizar(self, cadena):
        cadena = cadena + '$'
        self.listaErrores = []
        self.listaTokens = []
        self.i = 0
        while self.i < len(cadena):
            if self.estado == 0:
                self.s0(cadena[self.i])
            elif self.estado == 1:
                self.s1(cadena[self.i])
            elif self.estado == 2:
                self.s2(cadena[self.i])
            elif self.estado == 3:
                self.s3(cadena[self.i]) 
            elif self.estado == 4:
                self.s4(cadena[self.i])                   
            elif self.estado == 6:
                self.s6(cadena[self.i])            

            self.i += 1    

    def imprimirTokens(self):
        '''Imprime una tabla con los tokens'''
        x = PrettyTable()
        x.field_names = ["Lexema","Linea","Columna","Tipo"]
        for token in self.listaTokens:
            x.add_row([token.lexema, token.linea, token.columna,token.tipo])
        print(x)

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["Descripcion","Linea","Columna"]
        for error_ in self.listaErrores:
            x.add_row([error_.descripcion, error_.linea, error_.columna])
        print(x)        