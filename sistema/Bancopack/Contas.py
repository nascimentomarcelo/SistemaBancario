from Bancopack.ContaBancaria import ContaBancaria
    
class Contas(ContaBancaria):
    def _init_(self, numero, nome, cpf, saldo):
        self.numero = numero
        self.nome = nome
        self.cpf = cpf
        self.saldo = saldo

    def saque_verboso(self, value):
        print(self)
        self.sacar(value)
        
        saldo_atual = self.consultar_saldo()
        print(f"Saldo após o saque: R${saldo_atual:.2f}")