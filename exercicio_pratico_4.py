"""Armazena os dados para inscrição de um curso, mostra todos os dados cadastrados."""

from random import randint

#mostra o menu de opcoes
def menu():
  print("*" * 20, "MENU", "*" * 20)
  print("1 - Nova inscrição")
  print("2 - Vizualizar incrição")
  print("0 - Encerrar")

#faz o cadastro dos dados da pessoa
def cadastrar():
  voucher = randint(0000, 9999)
  nome = input("Digite seu nome: ")
  email = input("Digite seu email: ")
  telefone = int(input("Digite seu telefone: "))
  curso = input("Digite seu curso: ")
  dados = {"Voucher":voucher, "Nome":nome, "Email":email, "Telefone":telefone, "Curso":curso}
  return dados

#mostra todos os dados cadastrados
def mostrar(lista):
    print("-" * 20, "LISTA DE INSCRITOS", "-" * 20)
    if(lista != []):
     for cadastro in lista:
      for i,j in cadastro.items():
       print("{:<20}:  {:>20}" .format(i, j))
      print("\n")
    else:
      print("Nenhuma inscrição cadastrada")

#principal
lista = []
while True:
 menu()
 try:
  opcao = int(input("Opção escolhida: "))
  while(opcao > 2 or opcao < 0):
   print("Valor invalido")
   print("Digite 0, 1 ou 2 \n")
   opcao = int(input("Opção escolhida: "))
 except ValueError:
   print("Valor invalido")
   print("Digite 0, 1 ou 2 \n")
   continue
 if(opcao == 0):
   break
 if(opcao == 1):
  cadastro = cadastrar()
  lista.append(cadastro)
 if(opcao == 2):
  mostrar(lista)
print("\n")
print("Programa Encerrado!")