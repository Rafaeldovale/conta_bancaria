Opção = input('Qual operação Opção realizar: \n'
               '[d] Deposito \n'
               '[s] Saque \n'
               '[e] Extrato \n'
               '[q] Sair \n').strip().upper()

print('*=' * 20)


saldo = n_saque = 0
limite = 500
extrato = ""
limite_saque = 3

while Opção != 'Q':

    if Opção == 'D':
        valor = float(input('Qual o valor a ser depositado: R$ '))
        if valor > 0:
            saldo += valor 
            print('Deposito realizado com sucesso!')
        else:
            print('Valor não permitido para deposito!')

    elif Opção == 'S':
        saque = float(input('Qual o valor para saque: R$ '))
        if limite_saque > 0:
            if saque <= saldo:
                if saque <= limite:
                    saldo -= saque
                    limite_saque -= 1   
                    print('Saque realizado com Sucesso')
                else:
                    print(f'O limnite do saque é de R$ {limite_saque}')
            else:
                print(f'Saldo insuficiente! saldo = R$ {saldo}')
        else:
            print('Ja atingiu o limite diário para o saque')

    elif Opção == 'E':
        print('*=' * 20)
        print(f'Saldo Atual R$ {saldo:.2f}')
        print('*=' * 20)
    
    else:
        print('Opção Incorreta! Tenta novamente!')
        break

    print('*=' * 20)

    Opção = input('Qual operação Opção realizar: \n'
               '[d] Deposito \n'
               '[s] Saque \n'
               '[e] Extrato \n'
               '[q] Sair \n').strip().upper()

