#EDUARDO DIAZ DEL CASTILLO
import ply.lex as lex
import re
import codecs
import os
import sys
import types
import copy
import inspect


tokens = (
	'ID',
	'NUMERO',
	'SUMA',
	'RESTA',
	'PRODUCTO',
	'DIVISION',
	'IPARENTESIS',
	'DPARENTESIS',
	'IGUAL',
)

#Expresiones regulares
t_ID = r'\w+'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_PRODUCTO = r'\*'
t_DIVISION = r'/'
t_IPARENTESIS = r'\('
t_DPARENTESIS = r'\)'
t_IGUAL = r'='


#Expresion regular para numeros enteros
def t_NUMERO(t):
	r'\d+'
	t.value = int(t.value)
	return t

#evaluar varias lineas
def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

#ignora espacios y tabulacion
t_ignore = ' \t'

#manejo de errores, si un caracter no coincide con los tokens
def t_error(t):

	print("CARACTER INVALIDO '%s'"  % t.value[0])
	t.lexer.skip(1)
	print("\n******************************************")


#constructor del lexer
lexer = lex.lex()
