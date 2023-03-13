"""Converte as vogais do nome digitado em simbolos"""

#atributos
nome = input("Digite um nome: ")
nome_modificado = nome

if("a" in nome):
 nome_modificado = nome_modificado.replace('a', '@')
if("e" in nome):
 nome_modificado = nome_modificado.replace('e', '&')
if("i" in nome):
 nome_modificado = nome_modificado.replace('i', '!')
if("o" in nome):
 nome_modificado = nome_modificado.replace('o', '#')
if("u" in nome):
 nome_modificado = nome_modificado.replace('u', '*')

print(nome.upper())
print(nome_modificado.upper())
