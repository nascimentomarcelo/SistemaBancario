from abc import ABC, abstractmethod
from Bancopack.DadosInvalidosError import DadosInvalidosError
from Bancopack.TransacaoInvalidaError import TransacaoInvalidaError
from Bancopack.SaldoInsuficienteError import SaldoInsuficienteError
from Bancopack.Moeda import Moeda


# File: ContaBancaria.py
from abc import ABC, abstractmethod
from Bancopack.DadosInvalidosError import DadosInvalidosError
from Bancopack.TransacaoInvalidaError import TransacaoInvalidaError
from Bancopack.SaldoInsuficienteError import SaldoInsuficienteError

class ContaBancaria(ABC):
    num_contas = 0
    def __init__(self, nome, cpf, numero, saldo):
        self.numero = numero
        self.nome = nome
        self.cpf = cpf
        self.saldo = Moeda(saldo)

        if not numero or not nome or not saldo or not cpf:
            raise DadosInvalidosError("Os dados fornecidos são inválidos.")

    @abstractmethod
    def sacar(self, valor):
        if valor < 0:
            raise TransacaoInvalidaError("O valor de saque não pode ser negativo.")
        if valor > self.saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
        self.saldo -= valor

    @abstractmethod
    def depositar(self, valor):
        if valor < 0:
            raise TransacaoInvalidaError("O valor de depósito não pode ser negativo.")
        self.saldo += valor

    @abstractmethod
    def consultar_rendimento(self, dias):   #item 9
        rendimento = (self.saldo * self.taxa_rendimento * dias) / 30.0
        return rendimento

    def get_saldo(self):
        return self.saldo

    def consultar_rendimento(self, dias):   #item 9
        dias = input(int("digite o numero de dias: "))
        rendimento = (self.saldo * self.taxa_rendimento * dias) / 30.0
        return rendimento
    
    @property
    def numero(self):
        return self._numero

    @property
    def nome(self):
        return self._nome

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, novo_saldo):  #item 12
        if novo_saldo >= Moeda(0):
            self._saldo = novo_saldo
        else:
            raise ValueError("O saldo não pode ser negativo.")

    @numero.setter
    def numero(self, numero):
        self._numero = numero
        
    @nome.setter
    def nome(self, nome):
        self._nome = nome
        
    def sacar(self, valor):
        
        if valor < 0:
            raise TransacaoInvalidaError("O valor de saque não pode ser negativo.")
        
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para realizar o saque.")
        
        self._saldo -= valor

    def depositar(self, valor):
        if valor < 0:
            raise TransacaoInvalidaError("O valor de depósito não pode ser negativo.")
        self._saldo += valor

 
        
    