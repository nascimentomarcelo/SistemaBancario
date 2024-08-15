## Programação Orientada a Dados

Esse código, realizado em Python (versão 3.11), implementa uma solução para o gerenciamento de dados de clientes dentro de uma Fintech, e permite que sejam feitas operações financeiras diante dos dados fornecidos.

Marcelo Nascimento da Silva

Operações que poderão ser executadas:
Criação de contas corrente, poupança e investimento, que permitem realizar saque, depósito, consulta de saldo, atribuição e calculos de rendimento(conta investimento). Há também algumas restrições quanto ao número da conta que necessitam de 4 dígitos, o cpf de 11 dígitos, saldo de número positivo, e também, o nome do cliente ter no máximo 40 caracteres.

## Como usar o sistema:

Execute o código fornecendo o arquivo de entrada(1.txt, 2.txt);

O código irá processar o arquivo e realizar as operações bancárias necessárias;

Cada arquivo de entrada terá um arquivo de log correspondente com extensão .log e um arquivo de saída com extensão .saida;

Após processar todos os arquivos de entrada, o código exibirá as estatísticas sobre as contas criadas, incluindo o número total de contas, o número de contas correntes, o número de contas poupança e o número de contas de investimento.

Controle de erros:
O código é executado, e quando um erro é encontrado ele é registrado em log_pth. São eles: DadosInvalidosError: lançada quando os dados fornecidos são inválidos. ContaInexistenteError: lançada quando uma conta não existe ou não foi encontrada. SaldoInsuficienteError: lançada quando uma transação não pode ser concluída devido a saldo insuficiente ou limite excedido. TransacaoInvalidaError: lançada quando uma transação é inválida.
