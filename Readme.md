-- Desafio -- 

Fomos contratados por um grande banco para desenvolver o seu novo
sistema. Esse banco deseja modernizar suas operações e para isso
escolheu a linguagem Python. Para a primeira versão do sistema 
devemos implementar apenas 3 operações: Debito, saque e extrato.

Operação de depósito

Dever ser possível depoistar valores posistivos para a minha
conta bancária. A v1 do projeto trabalha apenas com 1 usuário, 
dessa forma não precisamos nos preocupar em identificar qual é
o número da agência e conta bancária. Todos os depósitos devem
ser armazenados em uma variável e exibidos na operação de extrato

Operação de saque

O sistema deve permirt realizar 3 saques diários com limite máximo
de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta,
o sistema deve exibir uma mensagem informando que não será possível
sacar o dinheiro por falata de saldo. Todos os saques devem ser
armazenados em uma variável e exibidos na operação de extrato.

Operação de extrato

Essa operação deve listar todos os depósitos e saques realizados
na conta. No fim da listagem deve ser exibido o saldo atual da conta
Os valores devem ser exibidos utilizando o formato R$ xxxx.xx,
exemplo:
1500.45 = R$ 1500.45

/********************************************************************/

--Desafio II--

Separar as funções exisstentes de saque, depósito e extrato em funções.
Criar duas novas fuções: cadastrar usuário(cliente) e cadastrar
conta bancária.

Precisamos deixar o código mais modularizado, para isso vamos criar 
funções para as operações existentes: sacar, depositar e visualizar 
histórico. Além disso, para versão 2 do sistema precimos criar duas novas
funções: criar usuário(cliente do bando) e criar conta corrrente
(vincular com usuário).

Saque

A função saue deve receber os argumentos apnas por nome (Keyword
only). Sugestão de argumentos: saldo, valor, extrato, limite, numero_
saque, limite_saques. Sugestão de retorno: Saldo e Extrato.

Depósito

A função depósito deve receber os argumentos apenas por posição
(positional only). Sugestão de argumentos: saldo, valor, extrato.
Sugestão de retorno: Saldo e Extrato.

Extrato

A função extrato deve receber os argumentos por posição e nome
(positional only e keyword only). Argumentos posicionais:
saldo, argumentos nomeados: extrato.

Novas Funções 

Precisamos criar duas novas funções: criar usuário e criar
conta corrente. Fique a vontade para adicionar mais funções,
exemplo: listar contas.

Criar usuário(cliente)

O programa deve armazenar os usuários em uma lista, um usuário
é composto por: nome, data de nascimento, cpf e endereço.
O endereço é uma string com o formato logradouro, nro - bairro -
cidade/sigla estado. Deve ser armazenado somente os número do 
CPF; Não podemos cadastrar  usuários com o mesmo CPF.

Criar Conta Corrente

O programa deve armazenar contas em uma lista, uma conta é 
composta por: agência, número da conta e usuário. O número da 
conta é sequencial, iniciando em 1. O número da agência é fixo:
"0001". O usuário pode ter mais de uma conta, mas uma conta pertence 
a somente um usuário.

Dica

Para vincular um usuário a uma conta, filtre a lista de usuários
buscando o número do CPF informado para cada usuário da lista.

/******************************************************************/

--Desafio III--

Com os novos conhecimentos adquiridos sobre data e hora, você foi 
encarregado de implemnetar as seguintes funcionalidades no sistemas:

- Estabelecer um limite de 10 transações diárias para uma conta.

- Se o usuário tentar fazer uma trans~ção após antigir o limite, deve
ser informado que excedeu o número de transações permitidas para aquele dia.

- Mostre no extrato, a data e hora de todas as transações.
