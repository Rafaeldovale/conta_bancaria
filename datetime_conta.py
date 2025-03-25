import datetime

# Listas globais para armazenar usuários e contas
usuarios = []
contas = []

# Função para registrar a data e hora de uma transação
def registrar_transacao(tipo, valor):
    data_hora = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    return f"{data_hora} - {tipo}: R$ {valor:.2f}"

# Função para saque
def sacar(numero_conta, valor):
    conta = next((conta for conta in contas if conta["numero_conta"] == numero_conta), None)
    if not conta:
        print("Conta não encontrada.")
        return

    if conta["transacoes_realizadas"] >= 10:
        print("Erro: Você excedeu o número de transações diárias permitidas (10).")
        return

    if valor > conta["saldo"]:
        print("Saldo insuficiente para realizar o saque.")
    elif valor > 500:  # Limite do saque
        print("O valor do saque excede o limite permitido.")
    elif valor <= 0:
        print("Valor inválido para saque.")
    else:
        conta["saldo"] -= valor
        conta["extrato"].append(registrar_transacao("Saque", valor))
        conta["transacoes_realizadas"] += 1
        print("Saque realizado com sucesso!")

# Função para depósito
def depositar(numero_conta, valor):
    conta = next((conta for conta in contas if conta["numero_conta"] == numero_conta), None)
    if not conta:
        print("Conta não encontrada.")
        return

    if conta["transacoes_realizadas"] >= 10:
        print("Erro: Você excedeu o número de transações diárias permitidas (10).")
        return

    if valor > 0:
        conta["saldo"] += valor
        conta["extrato"].append(registrar_transacao("Depósito", valor))
        conta["transacoes_realizadas"] += 1
        print("Depósito realizado com sucesso!")
    else:
        print("Valor inválido para depósito.")

# Função para exibir extrato
def exibir_extrato(numero_conta):
    conta = next((conta for conta in contas if conta["numero_conta"] == numero_conta), None)
    if not conta:
        print("Conta não encontrada.")
        return

    print("\n--- Extrato ---")
    if not conta["extrato"]:
        print("Não foram realizadas movimentações.")
    else:
        for transacao in conta["extrato"]:
            print(transacao)
    print(f"Saldo atual: R$ {conta['saldo']:.2f}")
    print("----------------")

# Função para criar usuário
def criar_usuario(nome, data_nascimento, cpf, endereco):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            print("Erro: Já existe um usuário com esse CPF.")
            return
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
            "usuario": usuario,
            "saldo": 0,
            "extrato": [],
            "transacoes_realizadas": 0
        })
        print(f"Conta criada com sucesso. Agência: 0001, Número da conta: {numero_conta}.")
    else:
        print("Erro: Usuário não encontrado. Certifique-se de que o CPF está correto.")

# Função para listar contas
def listar_contas():
    if contas:
        print("\n--- Lista de Contas ---")
        for conta in contas:
            print(f"Agência: {conta['agencia']}")
            print(f"Número da Conta: {conta['numero_conta']}")
            print(f"Titular: {conta['usuario']['nome']} (CPF: {conta['usuario']['cpf']})")
            print(f"Saldo: R$ {conta['saldo']:.2f}")
            print(f"Transações Diárias Realizadas: {conta['transacoes_realizadas']}/10")
            print("-" * 30)
    else:
        print("Nenhuma conta cadastrada ainda.")

# Função principal
def main():
    while True:
        print("\nEscolha a operação:")
        print("[d] Depósito\n[s] Saque\n[e] Extrato\n[u] Criar Usuário\n[c] Criar Conta\n[lc] Listar Contas\n[q] Sair")
        opcao = input("Digite a opção desejada: ").lower()

        if opcao == "d":
            numero_conta = int(input("Número da conta: "))
            valor = float(input("Informe o valor para depósito: R$ "))
            depositar(numero_conta, valor)

        elif opcao == "s":
            numero_conta = int(input("Número da conta: "))
            valor = float(input("Informe o valor para saque: R$ "))
            sacar(numero_conta=numero_conta, valor=valor)

        elif opcao == "e":
            numero_conta = int(input("Número da conta: "))
            exibir_extrato(numero_conta)

        elif opcao == "u":
            nome = input("Nome completo: ")
            data_nascimento = input("Data de nascimento (dd-mm-aaaa): ")
            cpf = input("CPF (somente números): ")
            endereco = input("Endereço (logradouro, nro - bairro - cidade/sigla estado): ")
            criar_usuario(nome, data_nascimento, cpf, endereco)

        elif opcao == "c":
            cpf = input("Informe o CPF do titular da conta: ")
            criar_conta(cpf)

        elif opcao == "lc":
            listar_contas()

        elif opcao == "q":
            print("Obrigado por usar o sistema bancário. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

# Executar o programa principal
if __name__ == "__main__":
    main()
