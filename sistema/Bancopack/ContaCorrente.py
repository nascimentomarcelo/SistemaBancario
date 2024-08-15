from Bancopack.DadosInvalidosError import DadosInvalidosError
from Bancopack.ContaBancaria import ContaBancaria
from Bancopack.Moeda import Moeda


class ContaCorrente(ContaBancaria):
    def __init__(self, nome, cpf, saldo, numero, limite_cheque_especial):
        super().__init__(nome, cpf, numero, saldo)
        self.limite_cheque_especial = Moeda(limite_cheque_especial)
        self.taxa_rendimento = 0.01  # Taxa de rendimento

        if not numero or not nome or not saldo or not cpf: #item 14
            raise DadosInvalidosError("Os dados fornecidos são inválidos.")
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        saldo_disponivel = self.saldo - self.limite_cheque_especial
        if valor <= saldo_disponivel:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        return self.saldo

    def aplicar_rendimento(self):
        rendimento = self.saldo * self.taxa_rendimento
        self.saldo += rendimento
 
    def consultar_rendimento(self, dias):   #item 9
        rendimento = (self.saldo * self.taxa_rendimento * dias) / 30.0
        return rendimento
        
    def saque_verboso(self, valor):
        pass

    def __str__(self):
        return f'Conta Corrente\nNúmero: {self.numero}\nNome: {self.nome}\nSaldo: R${self.saldo:.2f}\nLimite Cheque Especial: R${self.limite_cheque_especial:.2f}'



