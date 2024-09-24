import datetime
import pytz

class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.transacoes_diarias = 0
        self.timezone = pytz.timezone('America/Sao_Paulo')  # Substitua pelo seu fuso horário

    def depositar(self):
        if self.transacoes_diarias >= 10:
            print("Você atingiu o limite de transações diárias.")
            return
        while True:
            try:
                valor = float(input("Qual o valor será depositado? "))
                if valor > 0:
                    self.saldo += valor
                    self.registrar_transacao(f"Depósito: R$ {valor:.2f}")
                    break
                else:
                    print("Valor inválido. O valor do depósito deve ser positivo.")
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")

    def sacar(self):
        if self.transacoes_diarias >= 10:
            print("Você atingiu o limite de transações diárias.")
            return
        while True:
            try:
                valor = float(input("Qual o valor será sacado? "))
                if valor > 0 and valor <= 500:
                    if valor <= self.saldo:
                        self.saldo -= valor
                        self.registrar_transacao(f"Saque: R$ {valor:.2f}")
                        break
                    else:
                        print("Saldo insuficiente para saque!")
                else:
                    print("Valor inválido. O valor do saque deve ser positivo e menor ou igual a R$ 500,00.")
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")

    def imprimir_extrato(self):
        print("\n=== Extrato ===")
        for operacao, data_hora in self.extrato:
            print(f"{data_hora}: {operacao}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")

    def registrar_transacao(self, operacao):
        agora = datetime.datetime.now(self.timezone)
        self.extrato.append((operacao, agora.strftime("%d/%m/%Y %H:%M:%S")))
        self.transacoes_diarias += 1

# Criando uma instância da conta
conta = ContaBancaria()

# Menu principal
while True:
    print("\n=== Menu ===")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")
    opcao = int(input("Digite a opção desejada: "))

    if opcao == 1:
        conta.depositar()
    elif opcao == 2:
        conta.sacar()
    elif opcao == 3:
        conta.imprimir_extrato()
    elif opcao == 4:
        break
    else:
        print("Opção inválida.")