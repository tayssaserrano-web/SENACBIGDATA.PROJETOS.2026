# Atividade Boletim

# Solicita ao usuário que insira quatro notas,calcula a média dessas notas e exibe o resultado. 

# input: solicita ao usuário que insira um valor
# float: variável que recebe valores decimais

nome = (str(input("Digite seu nome: "))) # str é uma variável para receber textos ou uma cadeia de caracteres

nota1 = (float(input("Digite a primeira nota: ")))
nota2 = (float(input("Digite a segunda nota: "))) 
nota3 = (float(input("Digite a terceira nota: "))) 
nota4 = (float(input("Digite a quarta nota: "))) 

media = (nota1+nota2+nota3+nota4)/4 # / é o sinal de divisão
print("A média das notas é: ", media) # print exibe o resultado na tela

print("===== RESULTADO =====")
if media >= 7: # se a média for maior ou igual a 7, o aluno está aprovado
    print(f"{nome}, você está aprovado(a) :)")
elif media >= 5: # se a média for maior ou igual a 5, o aluno está de recuperação
    print(f"{nome}, você está de recuperação :/") 
else: # se a média for menor que 5, o aluno está reprovado
    print(f"{nome}, você está reprovado(a) ;-;")     