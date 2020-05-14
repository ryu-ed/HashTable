# HashTable - Tabla de Simbolos Python3

El programa identifica los tokens por medio de expresiones regulares, las cuales pueden ser expresadas facilmente en python.
En este caso en lugar de utilizar numeros como identificadores, utilice las expresiones regulares. 

_El programa da como resultado un arreglo lextoken que contiene lo siguiente: lextoken(token,caracter/cadena,fila,columna)_

_Las filas y columnas demuestran donde esta ubicado el token dentro del archivo de texto_
***Al descargar el proyecto, en ubuntu deben compilarlo de la siguiente manera en la terminal: python3 index.py diccionario.txt***

| **Token** | **Identificador = expresion regular** |  **Descripcion** |
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

## Captura de imagen del funcionamiento del programa
![alt text](https://github.com/ryu-ed/HashTable/raw/master/images/valid.PNG " ")

### Para ejecutar el programa se debe instalar o tener:
- Libreria ply: sudo apt-get install python3-ply
- python 3: https://python-guide-es.readthedocs.io/es/latest/starting/install3/linux.html
