from Bancopack.Moeda import *
from Bancopack.DadosInvalidosError import DadosInvalidosError
from Bancopack.ContaBancaria import ContaBancaria

class ContaInvestimento(ContaBancaria):
    def __init__(self, numero, nome, saldo, cpf, tipo_risco):
        super().__init__(numero, cpf, nome, saldo)
        self.cpf = cpf
        self.taxa_rendimento = self._definir_taxa_rendimento(tipo_risco)
        self.tipo_risco = "Baixo" 
        self.tipo_risco = "Medio"
        self.tipo_risco = "Alto"
        
        if not numero or not nome or not saldo or not cpf: #item 14
            raise DadosInvalidosError("Os dados fornecidos são invalidos.")

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente.")

    def consultar_saldo(self):
        return self.saldo
    
    def consultar_rendimento(self, dias):   #item 9
        rendimento = (self.saldo * self.taxa_rendimento * dias) / 30.0
        return rendimento
    
    def _definir_taxa_rendimento(self, tipo_risco): #item 10
        if tipo_risco == "Baixo":
            return 0.1
        elif tipo_risco == "Medio":
            return 0.25
        elif tipo_risco == "Alto":
            return 0.5
    

      