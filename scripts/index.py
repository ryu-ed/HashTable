#EDUARDO DIAZ DEL CASTILLO
#FIRST COMPILE PYTHON3 IN UBUNTU
#RULES IN TERMINAL:
#WRITE IN CONSOLE: python3 index.py diccionario.txt
import sys
from lexer import lexer


if __name__ == "__main__":

	file_name = sys.argv[1]
	f = open(file_name, 'r')

	#leer el archivo y lo pasa al lexer

	data = f.read()
	lexer.input(data)

	#recorre y compara todo
	#si no coincide - error

	while True:

		tok = lexer.token()
		if not tok:
			break
		print("CARACTER VALIDOS >>> ", tok)


print("Cantidad de caracteres en archivo: ",len(data))
