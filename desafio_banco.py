# Desafio Banco RBV

BOAS_VINDAS = print("-"*20,"Bem-Vindo ao Banco RBN!","-"*20)

print("-"*80)

limite_saque_dia = 3

LIMITE_VALOR_SAQUE = 500.00
saldo = 200.00

extrato = []

def banco(saldo, extrato, limite_saque_dia, LIMITE_VALOR_SAQUE):
    menu = int(input('''
    ---------Banco RBN----------
    |  [1]  DEPOSITO           |
    |  [2]  SAQUE              |
    |  [3]  EXTRATO            |
    |  [4]  SAIR               |
    ----------------------------\n\n
    >>> Digite a opção desejado: '''))

    while True:

        if menu == 1:
            deposito = int(input("O que deseja Depositar?: "))
            saldo += deposito
            extrato.append(deposito)
            print(f'o valor do seu é de {saldo:.2f}')
            
            back_menu = int(input("eu deposito foi realizado com sucesso !!!\n\nVoce deseja volta ao menu anterior ? Se sim [1] ou não [2]: "))
            
            if back_menu == 1:
                banco(saldo, extrato, limite_saque_dia, LIMITE_VALOR_SAQUE)
            elif back_menu == 2:
                print("Obrigado por utilizar nossa plataforma =)")
                break
            else:
                print("Voce não prestou atenção na pergunta anterior, agora Tchau !!!")
                break
            return saldo, extrato, limite_saque_dia, LIMITE_VALOR_SAQUE

        elif menu == 2:

            saque = int(input("Quanta queria sacar hoje ?: "))

            if saque <= LIMITE_VALOR_SAQUE and limite_saque_dia >= 1 and saldo >= 1 :    
                LIMITE_VALOR_SAQUE -= saque
                saldo -= saque
                limite_saque_dia -= 1
                extrato.append(saque)
                print(f'O valor do seu saldo ficou R$ {saldo}')
                back_menu = int(input("Voce deseja voltar ao menu anterior ? Se sim [1] ou não [2]: "))

                if back_menu == 1:
                    banco(saldo, extrato, limite_saque_dia, LIMITE_VALOR_SAQUE)
                    break
                elif back_menu == 2:
                    print("Obrigado por utilizar nossos serviços !!!")
                    break
                else:
                    print("Voce não prestou atenção na pergunta anterior, agora Tchau !!!")
                    break

            elif saque > LIMITE_VALOR_SAQUE:
                print("Valor passou do limite de R$ 500,00 de saque, por favor tente novamente !!")
                back_to_menu = int(input(f"O seu saldo para saque é de R${LIMITE_VALOR_SAQUE:.2f}\n\n Mesmo assim deseja volta para o menu principal ? Se sim [1] ou não [2]: "))
                
                if back_to_menu == 1:
                    banco(saldo, extrato, limite_saque_dia, LIMITE_VALOR_SAQUE)
                elif back_to_menu == 2:
                    print("Obrigado por utilizar nosso serviços ! :) ") 
                    break
                else:
                    print("Botão Errado Tchau !!!")
                    break
                
            elif limite_saque_dia == 0:
                print("Voce exedeu o limite de saques diario, Tente novamente amanhã !!!")
                break

            elif saldo == 0 or saldo < saque:
                back__menu = int(input("Voce não esta com saldo suficiente em conta para realiza saque!!\n\nMesmo assim deseja assim deseja voltar para o menu principal ? Se sim [1] não [2]: "))
                
                if back__menu == 1:
                    banco(saldo, extrato, limite_saque_dia, LIMITE_VALOR_SAQUE)
                else:
                    print("Obrigado por usar nossos serviço!! ;)")
                    break
            else:
                print("Valor inserido esta invalido, tente novamente!!!")
                break

            return saldo, extrato, limite_saque_dia, LIMITE_VALOR_SAQUE

        elif menu == 3:
            print('-'*20,'Extrato','-'*20)
            print(f"Saldo - R$ {saldo:.2f}\n\nDepositos realizados:{extrato[0]:.2f}\n\nSaques realizados: {extrato[1]:.2f}")
            break

        elif menu == 4:
            print("Obrigado por utilizar nosso serviços =) ")
            break

        else:
            print("""
            |**********************************************************|
            |Ta perdido amigo!!! escreve certo e volte ao começo :( !!!|
            |**********************************************************|
            """)
            break

banco(saldo, extrato, limite_saque_dia, LIMITE_VALOR_SAQUE)