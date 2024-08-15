class Moeda:
    def __init__(self, valor):
        self.valor=int(valor)

    def __add__(self, other):
        if isinstance(other, Moeda):
            return Moeda(self.valor + other.valor)
        elif isinstance(other, (int, float)):
            return Moeda(self.valor + other)
        else:
            raise TypeError("Operação não definida para o tipo de objeto fornecido!")
        
        
    def __sub__(self, other):
        if isinstance(other, Moeda):
            return Moeda(self.valor - other.valor)
        elif isinstance(other, (int, float)):
            return Moeda(self.valor - other)
        else:
            raise TypeError("Operação não definida para o tipo de objeto fornecido!")
        
    def __truediv__(self, other):
        if isinstance(other, Moeda):
            return Moeda(self.valor / other.valor)
        elif isinstance(other, (int, float)):
            return Moeda(self.valor / other)
        else:
            raise TypeError("Operação não definida para o tipo de objeto fornecido!")
        
    def __mul__(self, other):
        if isinstance(other, Moeda):
            return Moeda(self.valor * other.valor)
        elif isinstance(other, (int, float)):
            return Moeda(self.valor * other)
        else:
            raise TypeError("Operação não definida para o tipo de objeto fornecido!")
        
    def __eq__(self, other):
        if isinstance(other, Moeda):
            return self.valor == other.valor
        elif isinstance(other, (int, float)):
            return self.valor == other
        else:
            raise TypeError("Operação não definida para o tipo de objeto fornecido!")
        
    def __gt__(self, other):
        if isinstance(other, Moeda):
            return self.valor > other.valor
        elif isinstance(other, (int, float)):
            return self.valor > other
        else:
            raise TypeError("Operação não definida para o tipo de objeto fornecido!")
        
    def __ge__(self, other):
        if isinstance(other, Moeda):
            return self.valor >= other.valor
        elif isinstance(other, (int, float)):
            return self.valor >= other
        else:
            raise TypeError("Operação não definida para o tipo de objeto fornecido!")
        
    def __lt__(self, other):
        if isinstance(other, Moeda):
            return self.valor < other.valor
        elif isinstance(other, (int, float)):
            return self.valor < other
        else:
            raise TypeError("Operação não definida para o tipo de objeto fornecido!")
        
    
    def __str__(self) -> str:
        return f'M${self.valor:.2f}'