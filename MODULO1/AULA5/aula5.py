#Exercicio em Aula 

#exemplo 1
# nome = input("informe seu nome: ")
# #se eu quero usar varias vezes um determinado comando, usar uma variavel. senão pode usar o print
# if nome== "Tayssa": 
#     resposta= "Tayssa presente :)"
# elif nome== "Paula": 
#     resposta= "Paula presente :)"
# exemplo 2
# acabei de consertar o cod pq vi que qualquer numb maior que 12 ia ser capri
mes = int(input("Informe o mês de seu nascimento:"))

if mes==1:
    signo="Aquário"
elif mes==2:
    signo="Peixes"
elif mes==3:
    signo="Áries"
elif mes==4:
    signo="Touro"
elif mes==5:
    signo="Gêmeos"
elif mes==6:
    signo="Câncer"
elif mes==7:
    signo="Leão"
elif mes==8:
    signo="Virgem"
elif mes==9:
    signo="Libra"
elif mes==10:
    signo="Escorpião"
elif mes==11:
    signo="Sagitário"
elif mes==12:
    signo="Capricórnio"
else: #mudei o else para isso 
    print("Esse mês não existe!")
    signo = None

if signo: #acrescentei um if 
    print(f"Seu signo é {signo}.")


# estrutura alternativa macth/case exemplo:

# mes = int(input("Informe o mês de seu nascimento:"))

# match mes:
#     case 1:
#         signo="Aquário"
#     case 2:
#         signo="Áries"
#     case 3:
#         signo="Touro"
#     case 4:
#         signo="Gêmeos"
#     case 5:
#         signo="Câncer"
#     case _:
#         signo="Número de mês inválido"

# print(f"{signo}.")   



''''''' exercicio para entrgar ''''''''
# caso 1 print do numero de lampadas necessarias; definir as variaveis; constantes
#está no arq da aula 4 
# potencia= 3 
# largura= 
# comprimento= 
