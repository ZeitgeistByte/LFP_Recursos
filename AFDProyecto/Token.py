class Token:
    '''Clase TOken'''
    def __init__(self,lexema : str,linea : int,columna : int,tipo : str) -> None:
        self.lexema = lexema
        self.linea = linea
        self.columna = columna
        self.tipo = tipo

    def imprimirData(self):
        print(self.lexema, self.linea, self.columna, self.tipo)