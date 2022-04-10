def obtenerIntervalos(lista : list):
    retorno = []
    elemento = []
    for i,token in enumerate(lista):
        if token.tipo == 'menorQue':
            elemento.append(i)
        if token.tipo == 'mayorQue' and len(elemento) == 1:
            elemento.append(i)
            retorno.append(elemento)
            elemento = []
    return retorno

def obtenerTipo(lista : list):
    for i,token in enumerate(lista):
        if token.tipo == 'reservada_tipo':
            return lista[i+2].lexema[1:-1]

def crearEtiqueta(listaTokens: list):
    '''
    valor
    '''
    for i,token in enumerate(listaTokens):
        if token.lexema == 'valor':
            return '<label> {} </label>\n<br>\n'.format(listaTokens[i+2].lexema[1:-1])

def crearInputTexto(listaTokens: list):
    '''
    valor
    fondo
    '''
    fondo = '""'
    valor = '""'
    for i,token in enumerate(listaTokens):

        if token.lexema == 'fondo':
            fondo = listaTokens[i+2].lexema
        if token.lexema == 'valor':
            valor = listaTokens[i+2].lexema            

    return '<input type="text" value={} placeholder={} /><br />'.format(valor,fondo)


def crearOpcion(listaTokens: list):
    html = ''
    nombre = '""'
    lista = []
    for i,token in enumerate(listaTokens):
        if token.lexema == 'nombre':
            nombre = listaTokens[i+2].lexema[1:-1]
        if token.lexema == 'valores':
            lista = crearLista(listaTokens[i-1:])
    for item in lista:
        html += '\t<option>{}</option>\n'.format(item)
    return '''<label>{}</label>
    <select>
      {}
    </select>\n'''.format(nombre,html)    


def crearRadio(listaTokens: list):
    html = ''
    nombre = '""'
    lista = []
    for i,token in enumerate(listaTokens):
        if token.lexema == 'nombre':
            nombre = listaTokens[i+2].lexema[1:-1]
        if token.lexema == 'valores':
            lista = crearLista(listaTokens[i-1:])
    for item in lista:
        html += '\t<label> <input type="radio" /> {} </label>\n'.format(item)
    return '''
    <fieldset>
      <legend>{}</legend>
      {}
    </fieldset>\n    
    '''.format(nombre,html)

def crearBoton(listaTokens: list):
    evento = ''
    valor = ''
    for i,token in enumerate(listaTokens):
        if token.lexema == 'valor':
            valor = listaTokens[i+2].lexema
        if token.lexema == 'evento':
            evento = listaTokens[i+2].lexema[1:-1]+'()'
    return '<br/><br/><input type="button" onclick="{}" value={}/><br/>\n'.format(evento,valor)


def crearLista(listaTokens: list): 
    lista = []
    for i,token in enumerate(listaTokens):
        if token.tipo == "Cadena_'":
            lista.append(token.lexema[1:-1])
    return lista

def crearHTML(tokens):
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
    <form>
    '''
    listaIntervalos = obtenerIntervalos(tokens)
    for intervalo in listaIntervalos:
        tipo = obtenerTipo(tokens[intervalo[0]:intervalo[1]])
        if tipo == 'etiqueta':
            html += crearEtiqueta(tokens[intervalo[0]:intervalo[1]])
        elif tipo == 'texto':
            html += crearInputTexto(tokens[intervalo[0]:intervalo[1]])     
        elif tipo == 'grupo-option':
            html += crearOpcion(tokens[intervalo[0]:intervalo[1]]) 
        elif tipo == 'grupo-radio':
            html += crearRadio(tokens[intervalo[0]:intervalo[1]])     
        elif tipo == 'boton':
            html += crearBoton(tokens[intervalo[0]:intervalo[1]])                       

    html += '''
    </form>
    </body>
    </html>
    '''
    html_file = open('./AFDProyecto/index.html','w')
    html_file.write(html)
