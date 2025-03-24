usuarios = []
contas = []

# Função para saque
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Saldo insuficiente para realizar o saque.")
    elif valor > limite:
        print("O valor do saque excede o limite permitido.")
    elif numero_saques >= limite_saques:
        print("Número máximo de saques diários atingido.")
    elif valor <= 0:
        print("Valor inválido para saque.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_saques

# Função para depósito
def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")
    return saldo, extrato

# Função para exibir extrato
def exibir_extrato(saldo, /, *, extrato):
    print("\n--- Extrato ---")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("----------------")

# Função para criar usuário
def criar_usuario(nome, data_nascimento, cpf, endereco):

    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Erro: Já existe um usuário com esse CPF.")
            return
    # Adicionar o novo usuário à lista de usuários
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")

# Função para criar conta bancária
def criar_conta(cpf):
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    if usuario:
        numero_conta = len(contas) + 1
        contas.append({
            "agencia": "0001",
            "numero_conta": numero_conta,
            "usuario": usuario
        })
        print(f"Conta criada com sucesso. Agência: 0001, Número da conta: {numero_conta}.")
    else:
        print("Erro: Usuário não encontrado. Certifique-se de que o CPF está correto.")

def listar_usuarios():
    if usuarios:
        print("\n--- Lista de Usuários ---")
        for i, usuario in enumerate(usuarios, start=1):
            print(f"Usuário {i}:")
            print(f"  Nome: {usuario['nome']}")
            print(f"  Data de Nascimento: {usuario['data_nascimento']}")
            print(f"  CPF: {usuario['cpf']}")
            print(f"  Endereço: {usuario['endereco']}")
            print("-" * 30)
    else:
        print("Nenhum usuário cadastrado ainda.")


# Função principal que simula o sistema bancário
def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3

    while True:
        print("\nEscolha a operação:")
        print("[d] Depósito\n[s] Saque\n[e] Extrato\n[u] Criar Usuário\n[c] Criar Conta\n[l] Listar usuário\n[q] Sair")
        opcao = input("Digite a opção desejada: ").lower()

        if opcao == "d":
            valor = float(input("Informe o valor para depósito: R$ "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor para saque: R$ "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=limite_saques
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "u":
            nome = input("Nome completo: ")
            data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
            cpf = input("CPF (somente números): ")
            endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "c":
            cpf = input("Informe o CPF do titular da conta: ")
            criar_conta(cpf)

        
        elif opcao == "l":
            listar_usuarios()

        elif opcao == "q":
            print("Obrigado por usar o sistema bancário. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Para executar o programa principal
if __name__ == "__main__":
    main()
