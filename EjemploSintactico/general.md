# LISTA DE COMANDOS

CREAR BASE "baseEjemplo"

EN "baseEjemplo" CREAR TABLA "tablaEjemplo"

INSERTAR ("David",25) EN "baseEjemplo"."tablaEjemplo"

IMPRIMIR "identificador"."id"

# TABLA DE TOKENS

| Nombre                     | Descripción del patrón                                | Expresión regular | ejemplos                |
| -------------------------- | ----------------------------------------------------- | ----------------- | ----------------------- |
| Cadena                     | Una cadena de caracteres encerrada en comillas dobles | \\"[^.\\"]\*\\"   | "1" "ejemplo-1" ":v v:" |
| Punto                      | Un caracter '.'                                       | '.'               | .                       |
| ParentesisIzquierdo        | Un caracter '('                                       | '('               | (                       |
| ParentesisDerecho          | Un caracter ')'                                       | ')'               | )                       |
| Coma                       | Un caracter ','                                       | ','               | ,                       |
| CREAR                      | palabra CREAR                                         | CREAR             | CREAR                   |
| BASE                       | palabra BASE                                          | BASE              | BASE                    |
| EN                         | palabra EN                                            | EN                | EN                      |
| TABLA                      | palabra TABLA                                         | TABLA             | TABLA                   |
| INSERTAR                   | palabra INSERTAR                                      | INSERTAR          | INSERTAR                |
| IMPRIMIR                   | palabra IMPRIMIR                                      | IMPRIMIR          | IMPRIMIR                |
| Un número entero sin signo | Al menos un dígito                                    | \d+               | 3,12,65                 |

# Gramática

|               |     |                                                                                   |
| ------------- | --- | --------------------------------------------------------------------------------- |
| S             | ::= | INICIO                                                                            |
| INICIO        | ::= | CREACIONBASE                                                                      |
|               |     | \| CREACIONTABLA                                                                  |
|               |     | \| INSERCION                                                                      |
|               |     | \| IMPRESION                                                                      |
| CREACIONBASE  | ::= | pr_crear pr_base cadena                                                           |
| CREACIONTABLA | ::= | pr_en cadena pr_crear pr_tabla cadena                                             |
| INSERCION     | ::= | pr_insertar parentesisIzquierdo LISTA parentesisDerecho pr_en cadena punto cadena |
| LISTA         | ::= | VALOR LISTA'                                                                      |
| LISTA'        | ::= | coma VALOR LISTA'                                                                 |
| LISTA'        | ::= | epsilon                                                                           |
| VALOR         | ::= | cadena                                                                            |
|               |     | \| numero                                                                         |
| IMPRESION     | ::= | pr_imprimir cadena punto cadena                                                   |
