# Desafio Banco RBV
import textwrap


def menu():
    menu = """\t\t
                ---------Banco RBN----------
                |  [a]\tCRIAR USUARIO      |
                |  [cc]\tCRIAR CONTA       |
                |  [lc]\tLISTAS DE CONTAS  |
                |  [d]\tDEPOSITO           |
                |  [s]\tSAQUE              |
                |  [sd]\tSALDO             |
                |  [e]\tEXTRATO            |
                |  [sa]\tSAIR              |
                ----------------------------\n
                >>> Digite a opção desejado: """
    
    return input(textwrap.dedent(menu))

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente numero): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuario com esse CPF! @@@")
        return
    
    nome = input("Informe o nome completo")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, Nº - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuario criado com sucesso! ===")

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta["agencia"]}
            C/C:\t{conta["numero_conta"]}
            Titular:\t{conta["usuario"]["nome"]}
            """
    print("-" * 100)
    print(textwrap.dedent(linha))

def filtrar_usuario(cpf, usuario):
    usuario_filtrados = [usuario for usuario in usuario if usuario ["cpf"] == cpf]
    return usuario_filtrados[0] if usuario_filtrados else None

def criar_conta(agencia, numero_conta, usuario):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuario)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
   
def depositar(saldo, valor, extrato,/): 

    if valor > 0:
        saldo += valor 
        extrato += f"Deposito:\tR${valor:.2f}\n"
        print("\n@@@ Deposito realizado com sucesso! @@@")
    else:
        print("\n @@@ Operação falhou! o valor informado é invalido")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): # Deve ter uma interação com os valores do saldo

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Voce não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! o valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Numero maximo de saques excedido. @@@")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")

    else:
        print("\n@@@ Operação falhou! o valor informado é invalido. @@@")

    return saldo, extrato

def exibir_saldo():

    saldo = 200.00

    print(f"""
          __________________________
          |         Saldo          |
          |     R$ {saldo}         |
          |________________________|
          
          """)
    retorno = int(input("Voce deseja voltar ao menu anterior ? Se sim [1] ou não [2]: "))

    if retorno == 1:
        main()
    elif retorno == 2:
        print("Obrigado por utilizar nosso serviços")
    else:
        print("Clicou valor errado, Até mais !!! ;)")

def exibir_extrato(saldo,/,*, extrato):

    print("\n=================== EXTRATO ===================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=================================================")

def main():
   
    BOAS_VINDAS = print("-"*64,"\n", "-"*20,"Bem-Vindo ao Banco RBN!","-"*20,"\n", "-"*64)

    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        
        opcao = menu()
        
        if opcao == "a":
            criar_usuario(usuarios)
        elif opcao == "cc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)
            print(contas)

        elif opcao == "d":
            valor = float(input("Informe um valor para deposito"))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe um valor de saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )

        elif opcao == "sd":
            exibir_saldo()
            
        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "sa":
            print("Obrigado por utiliza nosso serviços :)")
            break

        else:
            print("""
            |**********************************************************|
            |Ta perdido amigo!!! escreve certo e volte ao começo :( !!!|
            |**********************************************************|
            """)
            break

main()