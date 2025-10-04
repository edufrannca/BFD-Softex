from abc import ABC, abstractmethod

# 1. Classe Abstrata
class ContaBancaria(ABC):
    def __init__(self, saldo_inicial=0):
        if saldo_inicial < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = saldo_inicial

    @property
    def saldo(self):
        return self._saldo

    @saldo.setter
    def saldo(self, valor):
        if valor < 0:
            raise ValueError("O saldo não pode ser negativo.")
        self._saldo = valor

    @abstractmethod
    def depositar(self, valor):
        pass

    @abstractmethod
    def sacar(self, valor):
        pass


# 2. Subclasse ContaCorrente
class ContaCorrente(ContaBancaria):
    def __init__(self, saldo_inicial=0, taxa_manutencao=2):
        super().__init__(saldo_inicial)
        self.taxa_manutencao = taxa_manutencao  # Taxa descontada após cada saque

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito realizado: R${valor:.2f}. Saldo atual: R${self.saldo:.2f}")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        valor_total = valor + self.taxa_manutencao
        if valor_total <= self.saldo:
            self.saldo -= valor_total
            print(f"Saque de R${valor:.2f} realizado com taxa de R${self.taxa_manutencao:.2f}. "
                  f"Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para saque.")


# 3. Subclasse ContaPoupanca
class ContaPoupanca(ContaBancaria):
    def __init__(self, saldo_inicial=0, juros=0.02):
        super().__init__(saldo_inicial)
        self.juros = juros  # Percentual de juros (ex: 2% -> 0.02)

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito realizado: R${valor:.2f}. Saldo atual: R${self.saldo:.2f}")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("Saldo insuficiente para saque.")

    def aplicar_juros(self):
        rendimento = self.saldo * self.juros
        self.saldo += rendimento
        print(f"Juros de {self.juros * 100:.0f}% aplicados: R${rendimento:.2f}. "
              f"Saldo atual: R${self.saldo:.2f}")


# 4. Teste do código
if __name__ == "__main__":
    print("=== Conta Corrente ===")
    conta_corrente = ContaCorrente(saldo_inicial=100, taxa_manutencao=5)
    conta_corrente.depositar(50)
    conta_corrente.sacar(30)

    print("\n=== Conta Poupança ===")
    conta_poupanca = ContaPoupanca(saldo_inicial=200, juros=0.03)
    conta_poupanca.depositar(100)
    conta_poupanca.aplicar_juros()
    conta_poupanca.sacar(50)

    print("\n=== Saldos Finais ===")
    print(f"Saldo Conta Corrente: R${conta_corrente.saldo:.2f}")
    print(f"Saldo Conta Poupança: R${conta_poupanca.saldo:.2f}")
