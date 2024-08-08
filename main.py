def sistema(bp):
    while True:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-SALA DO TEMPO=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        opcao = input("Digite a opção desejada (1 - Treinar, 2 - Ver BP, 3 - Sair): ")
        if opcao == "1":
            while True:
                bp = treinar(bp)
                opcao = input("Deseja treinar novamente? (Enter - SIM, 1 - NÃO): ")
                if opcao == "1":
                    break
        elif opcao == "2":
            ver_bp(bp)
        elif opcao == "3":
            print("FIM")
            break
        else:
            print("Opção inválida!")
def treinar(bp):

        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-MENU DE TREINO=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("Você entrou na sala do tempo!")
        print("Você pode treinar para aumentar seu BP!")
        print("Você tem 3 opções de treino:")
        print("1 - Treino leve (aumenta 100 BP)")
        print("2 - Treino moderado (aumenta 500 BP)")
        print("3 - Treino pesado (aumenta 1000 BP)")
        opcao = input("Digite a opção desejada: ")
        if opcao == "1":
            bp += 100
            print("Você treinou e aumentou seu BP em 100!")
        elif opcao == "2":
            bp += 500
            print("Você treinou e aumentou seu BP em 500!")
        elif opcao == "3":
            bp += 1000
            print("Você treinou e aumentou seu BP em 1000!")
        else:
            print("Opção inválida!")
        return bp
def ver_bp(bp):
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-SALA DO TEMPO=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
    print("Seu BP é: ", bp)
sistema(0)






