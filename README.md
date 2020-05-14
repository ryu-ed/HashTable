# HashTable - Tabla de Simbolos Python3

El programa identifica los tokens por medio de expresiones regulares, las cuales pueden ser expresadas facilmente en python.
En este caso en lugar de utilizar numeros como identificadores, utilice las expresiones regulares. 


| Token | Identificador = expresion regular |  :Descripcion: |
| ------------- | ------------- | ------------- |
| ID | t_ID = r'\w+'  | Reconoce cualquier caracter alfanumerico  |
| NUMERO | t_NUMERO = r'\d+'  | Reconoce cualquier numero de 0 a 9 |
| SUMA  | t_SUMA = r'\+'  | Reconoce caracteres con el simbolo + |
| RESTA| t_RESTA =  r'\-'  | Reconoce caracteres con el simbolo -|
| PRODUCTO  | t_PRODUCTO = r'\*'  | Reconoce caracteres con el simbolo * |
| DIVISION  | t_DIVISION = r'/'  | Reconoce caracteres con el simbolo / |
| IPARENTESIS | t_IPARENTESIS = r'\('  | Reconoce el parentesis izquierdo |
| DPARENTESIS | t_DPARENTESIS = r'\)' | Reconoce el parentesis derecho |
| IGUAL  | T_IGUAL = r'='  | Reconoce el signo de = |

Captura de imagen del funcionamiento del programa
