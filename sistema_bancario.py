class ContaBancaria:
    def __init__(self):
        self.saldo = 0.0
        self.extrato = []
        self.saques_diarios = 0

    def depositar(self):
        while True:
            try:
                valor = float(input("Qual o valor será depositado? "))
                if valor > 0:
                    self.saldo += valor
                    self.extrato.append(f"Depósito: R$ {valor:.2f}")
                    break
                else:
                    print("Valor inválido. O valor do depósito deve ser positivo.")
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")

    def sacar(self):
        if self.saques_diarios >= 3:
            print("Você atingiu o limite de saques diários.")
            return
        while True:
            try:
                valor = float(input("Qual o valor será sacado? "))
                if valor > 0 and valor <= 500:
                    if valor <= self.saldo:
                        self.saldo -= valor
                        self.extrato.append(f"Saque: R$ {valor:.2f}")
                        self.saques_diarios += 1
                        break
                    else:
                        print("Saldo insuficiente para saque!")
                else:
                    print("Valor inválido. O valor do saque deve ser positivo e menor ou igual a R$ 500,00.")
            except ValueError:
                print("Valor inválido. Por favor, digite um número.")

    def imprimir_extrato(self):
        print("\n=== Extrato ===")
        for operacao in self.extrato:
            print(operacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")

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