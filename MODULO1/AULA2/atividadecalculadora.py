
# while true: loop infinito para manter a calculadora em execução até que o usuário decida sair
while True:
    print("====== Calcule já! ======")

    print("Escolha a operação desejada:")

    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Sair")

    opcao = input("Digite o número da operação desejada: ")
    # primeira verificação: se a opção for "5", o programa deve encerrar o loop e sair da calculadora 
    if opcao == "5":
        print("Saindo da calculadora. Até logo!")
        break
    # segunda verificação: se a opção for entre "1" e "4", o programa deve solicitar os números e realizar a operação correspondente
    if opcao >= "1" and opcao <= "4":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        # terceira verificação: dependendo da opção escolhida, o programa realiza a operação correspondente e exibe o resultado
        if opcao == "1":
            resultado = num1 + num2
            print(f"O resultado da soma é: {resultado}")
        elif opcao == "2":
            resultado = num1 - num2
            print(f"O resultado da subtração é: {resultado}")
        elif opcao == "3":
            resultado = num1 * num2
            print(f"O resultado da multiplicação é: {resultado}")
        elif opcao == "4":
            if num2 != 0:
                resultado = num1 / num2
                print(f"O resultado da divisão é: {resultado}")
            else: # verificação adicional para evitar divisão por zero
                print("Erro: Divisão por zero não é permitida.")
    else: # caso a opção escolhida não seja válida, o programa exibe uma mensagem de erro e solicita que o usuário escolha uma opção válida
        print("Opção inválida. Por favor, escolha uma opção válida.")
