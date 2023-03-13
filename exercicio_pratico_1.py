"""De acordo com a idade, determina a etapa de ensino de determinada criança"""

while True:

 #atributos
 nome = input("Nome da criança: ")
 idade = int(input("Idade: "))

 #etapas de ensino
 if(idade >= 1 and idade <= 5) :
   educacao = "Educação Infantil"
 elif(idade >= 6 and idade <= 10) :
   educacao = "Ensino Fundamental I"
 elif(idade >= 11 and idade <= 14) :
   educacao = "Ensino Fundamental II"
 elif(idade >= 15) :
   educacao = "Ensino Médio"
 print(educacao)

 opcao = int(input("Deseja continuar?  0-Não  1-Sim  "))
 if(opcao == 0) :
   break
print("Finalizado!")