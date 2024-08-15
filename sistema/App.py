from Bancopack.saldoinsuficienteerror import SaldoInsuficienteError
from Bancopack.Moeda import Moeda
from sys import argv
from Bancopack.dadosinvalidoserror import DadosInvalidosError
from Bancopack.containexistenteerror import ContaInexistenteError
from Bancopack.ContaInvestimento import ContaInvestimento
from Bancopack.ContaPoupanca import ContaPoupanca
from Bancopack.contaCorrente import ContaCorrente
from Bancopack.transacaoinvalidaerror import TransacaoInvalidaError

CCorrente, CPoupanca, CInvestimento = [], [], []

def criar_conta(dados_conta):
    if dados_conta['tipo'] == "contaCorrente":
        return ContaCorrente(
            dados_conta['nome'], dados_conta['cpf'], 
            dados_conta['saldo'], dados_conta['numero'], 
            dados_conta['limite_cheque_especial']
        )

    elif dados_conta['tipo'] == "contaPoupanca":
        return ContaPoupanca(
            dados_conta['nome'], dados_conta['cpf'], 
            dados_conta['saldo'], dados_conta['numero'], 
            dados_conta['taxa_rendimento']
        )

    elif dados_conta['tipo'] == "contaInvestimento":
        return ContaInvestimento(
            dados_conta['nome'], dados_conta['cpf'], 
            dados_conta['saldo'], dados_conta['numero'], 
            dados_conta['tipo_risco']
        )


for a in argv[1:]:
    conta_corrente, conta_poupanca, conta_investimento = None, None, None
    path_to_file = a
    log_pth = path_to_file.replace(".txt", ".log").replace("data", "out")
    saida_pth = path_to_file.replace(".txt", ".saida").replace("data", "out")
    
    log_file = open(log_pth, "w")
    log_file.write("Log de Execucao\n")

    file_saida = open(saida_pth, "w")
    file_saida.write("Saida do Programa\n")
        
    file = open(path_to_file, "r");

    nome = file.readline().split(":")[1].replace("\n", "").strip()
    if len(nome) > 50:
        DadosInvalidosError("Nome Invalido.", log_file)
        continue
    
    cpf = file.readline().split("->")[1].strip().replace("\n", "")
    if len(cpf) != 11:
        DadosInvalidosError("CPF Invalido.", log_file)
        continue
    
    conta_em_criacao = {} # dicionarico com dados para criação de um nova conta
    for line in file.readlines():
        spl = line.split("->")
        comando = spl[0].strip()
        atributo = spl[1].strip()
        
        if len(spl) > 2:
            valor = spl[2].strip()
            valor = Moeda(valor)
        
        # verifica se o comando começa com atribuir
        if comando.startswith("atribuir"):
            # remove o "atribuir " do comando
            comando = comando.replace("atribuir ", "")
            if comando == 'saldoInicial':
                conta_em_criacao['saldo'] = atributo
            elif comando == 'id da conta':
                conta_em_criacao['numero'] = atributo
            elif comando == 'limiteChequeEspecial':
                conta_em_criacao['limite_cheque_especial'] = atributo
            elif comando == 'taxaRendimento':
                conta_em_criacao['taxa_rendimento'] = atributo
            elif comando == 'tipoRisco':
                conta_em_criacao['tipo_risco'] = atributo
            else:
                DadosInvalidosError("Comando Invalido.", log_file)
                break
            continue
        elif conta_em_criacao != {}:
            log_file.write(f"Conta será criado com os dados: {conta_em_criacao}\n")
            # se o comando não for atribuir e já tiver uma conta em criação, cria a conta
            if conta_em_criacao['tipo'] == "contaCorrente":
                conta_corrente = criar_conta(conta_em_criacao)
                CCorrente.append(conta_corrente)
            elif conta_em_criacao['tipo'] == "contaPoupanca":
                conta_poupanca = criar_conta(conta_em_criacao)
                CPoupanca.append(conta_poupanca)
            elif conta_em_criacao['tipo'] == "contaInvestimento":
                conta_investimento = criar_conta(conta_em_criacao)
                CInvestimento.append(conta_investimento)
            conta_em_criacao = {}
        
        if comando == "criar uma":
            log_file.write(f"Iniciando criação de uma: {atributo}\n")
            conta_em_criacao['tipo'] = atributo
            conta_em_criacao['nome'] = nome
            conta_em_criacao['cpf'] = cpf
            
        elif comando == "consultar saldo":
            log_file.write(f"Consultando saldo da conta: {atributo}\n")
            try:
                if atributo == "contaCorrente":
                    saldo = conta_corrente.consultar_saldo()
                elif atributo == "contaInvestimento":
                    saldo = conta_investimento.consultar_saldo()
                elif atributo == "contaPoupanca":
                    saldo = conta_poupanca.consultar_saldo()
                
                file_saida.write(f"Saldo da conta {atributo}: {saldo}\n")
                
            except Exception as e:
                ContaInexistenteError("Operacao de consulta de saldo deu errado pois a Conta eh Inexistente.", log_file)
        
        elif comando == "calcular rendimento":
            log_file.write(f"Calculando rendimento da conta: {atributo}\n")
            try:
                c, days = atributo.split(":")
                days = int(days.split(" ")[1])
                if c == "contaCorrente":
                    rendimento = conta_corrente.consultar_rendimento(days)
                    
                elif c == "contaInvestimento":
                    rendimento = conta_investimento.consultar_rendimento(days)
                    
                elif c == "contaPoupanca":
                    rendimento = conta_poupanca.consultar_rendimento(days)
                    
                file_saida.write(f"Rendimento da conta {atributo}: {rendimento}\n")
                    
            except Exception as e:
                ContaInexistenteError("Operacao de consulta de rendimento deu errado pois a Conta eh Inexistente.", log_file)
        
        elif comando == "realizar saque":
            log_file.write(f"Realizando saque da conta: {atributo}\n")
            try:
                if atributo == "contaCorrente":
                    conta_corrente.saque_verboso(valor)
                    
                elif atributo == "contaInvestimento":
                    conta_investimento.sacar(valor)

                elif atributo == "contaPoupanca":
                    conta_poupanca.sacar(valor)

                file_saida.write(f"Valor do saque {atributo}: {valor}\n")

            except Exception as e:
                SaldoInsuficienteError("Operacao nao concluida por falta de saldo ou excedeu o limite.", log_file)
                
    
        elif comando == "realizar deposito":
            log_file.write(f"Realizando deposito da conta: {atributo}\n")
            try:
                if valor < 0:
                    DadosInvalidosError("O valor de deposito nao pode ser negativo.", log_file) 
                    break
                    
                if atributo == "contaCorrente":
                    print(valor)
                    conta_corrente.depositar(valor)

                elif atributo == "contaInvestimento":
                    conta_investimento.depositar(valor)

                elif atributo == "contaPoupanca":
                    conta_poupanca.depositar(valor)

                file_saida.write(f"Valor do deposito {atributo}: {valor}\n")

            except Exception as e:
                TransacaoInvalidaError("Insucesso no deposito.", log_file)
                break
    
    if conta_em_criacao != {}:
        # se o comando não for atribuir e já tiver uma conta em criação, cria a conta
        if conta_em_criacao['tipo'] == "contaCorrente":
            conta_corrente = criar_conta(conta_em_criacao)
            CCorrente.append(conta_corrente)
        elif conta_em_criacao['tipo'] == "contaPoupanca":
            conta_poupanca = criar_conta(conta_em_criacao)
            CPoupanca.append(conta_poupanca)
        elif conta_em_criacao['tipo'] == "contaInvestimento":
            conta_investimento = criar_conta(conta_em_criacao)
            CInvestimento.append(conta_investimento)

    file.close()
    log_file.close()
    file_saida.close()

    # imprimir o saldo final da conta investimento 
    with open(saida_pth, 'a') as f:
        f.write(f"Saldo final da conta investimento: {conta_investimento.consultar_saldo()}\n")

print("Contas Criadas:", len(CCorrente) + len(CPoupanca) + len(CInvestimento))
print("Contas Correntes:", len(CCorrente))
print("Contas Poupança:", len(CPoupanca))
print("Contas Investimento:", len(CInvestimento))