from prettytable import PrettyTable
from bases import *

class AnalizadorSintactico:

    def __init__(self,tokens : list) -> None:
        self.errores = []
        self.tokens = tokens

    def agregarError(self,esperado,obtenido):
        self.errores.append(
            '''ERROR SINTÁCTICO: se obtuvo {} se esperaba {}'''.format(obtenido,esperado)
        )

    def sacarToken(self):
        ''' Saca el primer token y lo quita de la lista'''
        try:
            return self.tokens.pop(0)
        except:
            return None

    def observarToken(self):
        ''' Saca el primer token y lo mete de nuevo en de la lista'''
        try:
            return self.tokens[0]
        except:
            return None

    
    def analizar(self):
        self.S()

    def S(self):
        self.INICIO()

    def INICIO(self):
        # Observar el primer elemento para
        # decidir a donde ir
        temporal = self.observarToken()
        if temporal is None:
            self.agregarError("reservada_CREAR | reservada_EN | reservada_INSERTAR | reservada_IMPRIMIR ","EOF")
        elif temporal.tipo == 'reservada_CREAR':
            self.CREACIONBASE()
        elif temporal.tipo == 'reservada_EN':
            self.CREACIONTABLA()
        elif temporal.tipo == 'reservada_INSERTAR':
            self.INSERCION()
        elif temporal.tipo == 'reservada_IMPRIMIR':
            self.IMPRESION()
        else:
            self.agregarError("reservada_CREAR | reservada_EN | reservada_INSERTAR | reservada_IMPRIMIR",temporal.tipo)

    def CREACIONBASE(self):
        # Comando de creación de base de datos
        # Producción
        #           CREACIONBASE	::=	pr_crear pr_base cadena

        # Sacar token --- se espera reservada_CREAR
        token = self.sacarToken()
        if token.tipo == 'reservada_CREAR':
            # Sacar otro token --- se espera reservada_BASE
            token = self.sacarToken()
            if token is None:
                self.agregarError("reservada_BASE","EOF")
                return
            elif token.tipo == "reservada_BASE":
                # Sacar otro token --- se espera cadena
                token = self.sacarToken()
                if token is None:
                    self.agregarError("cadena","EOF")
                    return
                elif token.tipo == "cadena":
                    #Llamo a mi funcionalidad
                    createDB(token.lexema)
                else:
                    self.agregarError("cadena",token.tipo)
            else:
                self.agregarError("reservada_BASE",token.tipo)
        else:
            self.agregarError("reservada_CREAR","EOF")
        


    def CREACIONTABLA(self):
        # Comando de creación de tabla en base de datos
        # Producción
        #           CREACIONTABLA	::=	pr_en cadena pr_crear pr_tabla cadena

        nombre_base = ''
        nombre_tabla = ''
        # Sacar token --- se espera reservada_EN
        token = self.sacarToken()
        if token.tipo == 'reservada_EN':
            # Sacar otro token --- se espera cadena
            token = self.sacarToken()
            if token is None:
                self.agregarError("cadena","EOF")
                return
            elif token.tipo == "cadena":
                nombre_base = token.lexema
                # Sacar otro token --- se espera reservada_CREAR
                token = self.sacarToken()
                if token is None:
                    self.agregarError("reservada_CREAR","EOF")
                    return
                elif token.tipo == "reservada_CREAR":
                    # Sacar otro token --- se espera reservada_TABLA
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("reservada_TABLA","EOF")
                        return
                    elif token.tipo == "reservada_TABLA":
                        # Sacar otro token --- se espera cadena
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("cadena","EOF")
                            return
                        elif token.tipo == "cadena":
                            nombre_tabla = token.lexema
                            #FUncionalidad
                            createTable(nombre_tabla,nombre_base)
                        else:
                            self.agregarError("cadena",token.tipo)   
                    else:
                        self.agregarError("reservada_TABLA",token.tipo)                    
                else:
                    self.agregarError("reservada_CREAR",token.tipo)
            else:
                self.agregarError("reservada_BASE",token.tipo)
        else:
            self.agregarError("reservada_EN","EOF")        


    def INSERCION(self):
        # Producción
        #INSERCION	::=	pr_insertar parentesisIzquierdo LISTA parentesisDerecho pr_en cadena punto cadena
        
        lista = None
        nombre_base = ''
        nombre_tabla = ''

        # Sacar token --- se espera reservada_INSERTAR
        token = self.sacarToken()
        if token.tipo == 'reservada_INSERTAR':
            # Sacar otro token --- se espera parentesisIzquierdo
            token = self.sacarToken()
            if token is None:
                self.agregarError("parentesisIzquierdo","EOF")
                return
            elif token.tipo == "parentesisIzquierdo":
                # Toca visitar NO TERMINAL -> LISTA
                # En lista espero un objeto python tipo lista []
                # Si recibo None quiere decir que hubo errores
                # Entonces retorno y no ejecuto nada
                lista = self.LISTA()
                if lista is None:
                    return
                # Sacar otro token --- se espera parentesisDerecho
                token = self.sacarToken()
                if token is None:
                    self.agregarError("parentesisDerecho","EOF")
                    return
                elif token.tipo == "parentesisDerecho":
                    # Sacar otro token --- se espera reservada_EN
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("reservada_EN","EOF")
                        return
                    elif token.tipo == "reservada_EN":
                        # Sacar otro token --- se espera cadena
                        token = self.sacarToken()
                        if token is None:
                            self.agregarError("cadena","EOF")
                            return
                        elif token.tipo == "cadena":
                            nombre_base = token.lexema
                            # Sacar otro token --- se espera punto
                            token = self.sacarToken()
                            if token is None:
                                self.agregarError("punto","EOF")
                                return
                            elif token.tipo == "punto":
                                # Sacar otro token --- se espera cadena
                                token = self.sacarToken()
                                if token is None:
                                    self.agregarError("cadena","EOF")
                                    return
                                elif token.tipo == "cadena":
                                    nombre_tabla = token.lexema
                                    insertar(nombre_tabla,nombre_base,lista)
                                else:
                                    self.agregarError("cadena",token.tipo)     
                            else:
                                self.agregarError("punto",token.tipo)                  
                        else:
                            self.agregarError("cadena",token.tipo)                             
                    else:
                        self.agregarError("reservada_EN",token.tipo)                     
                else:
                    self.agregarError("parentesisDerecho",token.tipo)                         
            else:
                self.agregarError("parentesisIzquierdo",token.tipo)          
        else:
            self.agregarError("reservada_INSERTAR","EOF")                

    def LISTA(self):
        # Producción
        #            LISTA' ::= VALOR LISTA'
        #Valor es un str o un int
        valor = self.VALOR()
        if valor is None:
            return
        
        lista_ = self.LISTA_()
        if lista_ is None:
            return        
                  #[3]    + [1,3,4]
                  #[3,1,3,4]
        return [valor] + lista_

    def LISTA_(self):
        # Producción
        #            LISTA' ::= coma VALOR LISTA' | epsilon
        
        #Para no perder el token en caso de irnos por epsilon, solo lo observo
        token = self.observarToken()
        if token is None:
            return
        if token.tipo == 'coma':
            #Ya se que es una coma entonces si lo saco
            token = self.sacarToken()

            #Llamamos al no terminal VALOR
            # Valor retorna un numero o una cadena
            valor = self.VALOR()
            #Si el valor es None quiere decir que hubo un error sintactico en VALOR
            #Entonces seguimos 'subiendo' ese None
            if valor is None:
                return
            
            lista_prima = self.LISTA_()

            #Si el valor es None quiere decir que hubo un error sintactico en LISTA'    
            if lista_prima is None:
                return
                
            #Retornamos una lista con lo obtenido en VALOR Y LISTA'
            return [valor] + lista_prima
        else:
            # Como en está producción es posible esperar un epsilon
            # Voy a retornar una lista vacía en caso de que token.tipo
            # no     sea una coma, esto para simular el epsilon
            return []
    

    def VALOR(self):
        # Producción
        #            VALOR ::= cadena | numero
              
        token = self.sacarToken()
        # Si no viene un token retornamos None para
        # Causar que no se ejecute el comando
        if token is None:
            self.agregarError("cadena | entero","EOF") 
            return
        if token.tipo == 'cadena':
            return token.lexema
        elif token.tipo == 'entero':
            return int(token.lexema)
        else:
            self.agregarError("cadena | entero",token.tipo) 

    def IMPRESION(self):
        # Comando de impresión de tabla en base de datos
        # Producción
        #           IMPRESION	::=	pr_imprimir cadena punto cadena      
        nombre_base = ''
        nombre_tabla = ''
        # Sacar token --- se espera reservada_IMPRIMIR
        token = self.sacarToken()
        if token.tipo == 'reservada_IMPRIMIR':
            # Sacar otro token --- se espera cadena
            token = self.sacarToken()
            if token is None:
                self.agregarError("cadena","EOF")
                return
            elif token.tipo == "cadena":
                nombre_base = token.lexema
                # Sacar otro token --- se espera punto
                token = self.sacarToken()
                if token is None:
                    self.agregarError("punto","EOF")
                    return
                elif token.tipo == "punto":
                    # Sacar otro token --- se espera cadena
                    token = self.sacarToken()
                    if token is None:
                        self.agregarError("cadena","EOF")
                        return
                    elif token.tipo == "cadena":
                        nombre_tabla = token.lexema
                        #llamar a funcionalidad de imprimir
                        imprimir(nombre_tabla,nombre_base)
                    else:
                        self.agregarError("cadena",token.tipo)     
                else:
                    self.agregarError("punto",token.tipo)                  
            else:
                self.agregarError("cadena",token.tipo)           
        else:
            self.agregarError("reservada_IMPRIMIR","EOF")                

    def imprimirErrores(self):
        '''Imprime una tabla con los errores'''
        x = PrettyTable()
        x.field_names = ["Descripcion"]
        for error_ in self.errores:
            x.add_row([error_])
        print(x)            