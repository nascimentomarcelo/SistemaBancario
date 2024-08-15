
from Bancopack.Moeda import *
from Bancopack.DadosInvalidosError import DadosInvalidosError
from Bancopack.ContaBancaria import ContaBancaria


class ContaPoupanca(ContaBancaria):
    def __init__(self, numero, nome, saldo, cpf, taxa_rendimento=0.0):
        super().__init__(nome, cpf, numero,  saldo)
        self.cpf = cpf
        self.taxa_rendimento = taxa_rendimento

        if not numero or not nome or not saldo or not cpf: #item 14
            raise DadosInvalidosError("Os dados fornecidos são inválidos.")   

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        return self.saldo
    
    def aplicar_rendimento(self):
        rendimento = self.saldo * self.taxa_rendimento
        self.saldo += rendimento

    def consultar_rendimento(self, dias):   #item 9
        dias = input(int("digite o numero de dias: "))
        rendimento = (self.saldo * self.taxa_rendimento * dias) / 30.0
        return rendimento
