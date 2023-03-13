"""Um jogo que é popular entre as crianças: um hotel onde os hóspedes
têm algumas restrições quanto a localização de seu quarto, seguindo as seguintes regras:
• O rato não pode ficar ao lado do gato.
• O cão não pode ficar ao lado do osso.
• O gato não pode ficar ao lado do cão.
• O queijo não pode ficar ao lado do rato
O jogo é composto por 4 fases, onde cada fase (a partir da fase 2) só é desbloqueada se a
anterior for concluída com êxito.
Em todas as fases, as células em * representam os quartos indisponíveis, portanto não
podem ser alocados. As letras nas células correspondem aos seguintes hóspedes: 
"""

#regras da fase 1
def fase_1() :
  print("Bem vindos a fase 1!")
  print("Na fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os quartos: ")
  lista = [['*', '*', '-', 'G'],['R', '-', '*', '*']]
  print(lista[0])
  print(lista[1])
  
  posicao_R = int(input("Em qual posição quer alocar o Rato ? "))
  while(posicao_R != 3 and posicao_R != 6) :
   print("Não pode alocar nesta posição")
   posicao_R = int(input("Em qual posição quer alocar o Rato ? "))

  posicao_G = int(input("Em qual posição quer alocar o Gato ? "))
  while(posicao_G != 3 and posicao_G != 6 or posicao_R == posicao_G) :
   print("Não pode alocar nesta posição")
   posicao_G = int(input("Em qual posição quer alocar o Gato ? "))

  if(posicao_R == 6 and posicao_G == 3) :
    print("Parabens, passou de fase \n")
  elif(posicao_R == 3 and posicao_G == 6) :
    print("game over")
    return False

#regras da fase 2
def fase_2() :
  print("Bem vindos a fase 2!")
  print("Na fase 2, o jogador deve alocar o CÃO, CÃO e o OSSO na seguinte matriz que representa os quartos: ")
  lista = [['-', '*', '*', '*'],['*', 'C', '-', '-']]
  print(lista[0])
  print(lista[1])
  
  posicao_C1 = int(input("Em qual posição quer alocar o CÃO ? "))
  while(posicao_C1 != 1 and posicao_C1 != 7 and posicao_C1 != 8) :
   print("Não pode alocar nesta posição")
   posicao_C1 = int(input("Em qual posição quer alocar o CÃO ? "))

  posicao_C2 = int(input("Em qual posição quer alocar o CÃO ? "))
  while(posicao_C2 != 1 and posicao_C2 != 7 and posicao_C2 != 8 or posicao_C2 == posicao_C1) :
   print("Não pode alocar nesta posição")
   posicao_C2 = int(input("Em qual posição quer alocar o CÃO ? "))

  posicao_O = int(input("Em qual posição quer alocar o OSSO ? "))
  while(posicao_O != 1 and posicao_O != 7 and posicao_O != 8 or posicao_O == posicao_C1 or posicao_O == posicao_C2) :
   print("Não pode alocar nesta posição")
   posicao_O = int(input("Em qual posição quer alocar o OSSO ? "))

  if(posicao_O == 1) :
    print("passou de fase \n")
  elif(posicao_O == 7 or posicao_O == 8) :
    print("game over")
    return False

#regras da fase 3
def fase_3() :
  print("Bem vindos a fase 3!")
  print("Na fase 3, o jogador deve alocar o GATO, RATO e o OSSO na seguinte matriz que representa os quartos: ")
  lista = [['-', '*', '*', '*'],['-', 'G', '-', '*']]
  print(lista[0])
  print(lista[1])
  
  posicao_G = int(input("Em qual posição quer alocar o GATO ? "))
  while(posicao_G != 1 and posicao_G != 5 and posicao_G != 7) :
   print("Não pode alocar nesta posição")
   posicao_G = int(input("Em qual posição quer alocar o CÃO ? "))

  posicao_R = int(input("Em qual posição quer alocar o RATO ? "))
  while(posicao_R != 1 and posicao_R != 5 and posicao_R != 7 or posicao_R == posicao_G) :
   print("Não pode alocar nesta posição")
   posicao_R = int(input("Em qual posição quer alocar o RATO ? "))

  posicao_O = int(input("Em qual posição quer alocar o OSSO ? "))
  while(posicao_O != 1 and posicao_O != 5 and posicao_O != 7 or posicao_O == posicao_R or posicao_O == posicao_G) :
   print("Não pode alocar nesta posição")
   posicao_O = int(input("Em qual posição quer alocar o OSSO ? "))

  if(posicao_R == 1) :
    print("passou de fase \n")
  elif(posicao_R == 5 or posicao_R == 8) :
    print("game over")
    return False

#regras da fase 4
def fase_4() :
  print("Bem vindos a fase 4!")
  print("Na fase 4, o jogador deve alocar o QUEIJO, QUEIJO e o OSSO na seguinte matriz que representa os quartos: ")
  lista = [['-', '-', '-', '*'],['*', 'R', '*', '*']]
  print(lista[0])
  print(lista[1])
  
  posicao_Q1 = int(input("Em qual posição quer alocar o QUEIJO ? "))
  while(posicao_Q1 != 1 and posicao_Q1 != 2 and posicao_Q1 != 3) :
   print("Não pode alocar nesta posição")
   posicao_Q1 = int(input("Em qual posição quer alocar o QUEIJO ? "))
  
  posicao_Q2 = int(input("Em qual posição quer alocar o QUEIJO ? "))
  while(posicao_Q2 != 1 and posicao_Q2 != 2 and posicao_Q2 != 3 or posicao_Q2 == posicao_Q1) :
   print("Não pode alocar nesta posição")
   posicao_Q2 = int(input("Em qual posição quer alocar o QUEIJO ? "))
    
  posicao_O = int(input("Em qual posição quer alocar o OSSO ? "))
  while(posicao_O != 1 and posicao_O != 2 and posicao_O != 3 or posicao_O == posicao_Q1 or posicao_O == posicao_Q2) :
   print("Não pode alocar nesta posição")
   posicao_O = int(input("Em qual posição quer alocar o OSSO ? "))

  if(posicao_O == 2) :
    print("Parabêns, você ganhou!")
    return False
  elif(posicao_Q1 == 2 or posicao_Q2 == 2) :
    print("game over")
    return False

#mostra menu inicial
def menu():
 print("    HOTEL DOS ANIMAIS")
 print("Especificando posição:")
 vetor = [1,2,3,4,5,6,7,8]
 print(vetor[0:4])
 print(vetor[4:8], "\n")

#principal
while(True):
 menu()
 if(fase_1() == False):
   break
 elif(fase_2() == False):
   break
 elif(fase_3() == False):
   break
 elif(fase_4() == False):
   break