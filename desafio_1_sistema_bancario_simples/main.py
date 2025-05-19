class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class ContaBancaria:
    def __init__(self, numero_conta, cliente):
        self.numero_conta = numero_conta
        self.cliente = cliente
        self.saldo = 0.0


    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        
        self.saldo -= valor
        return True

    def exibir_saldo(self):
        return self.saldo
    

def main():
    client1 = Cliente("Laezio", 25)

    print(f"Bem vindo, {client1.nome}")

    conta = ContaBancaria(1234, client1.nome)


    while True:
        print("\n Menu: ")
        print("1. Depositar")
        print("2. Sacar")
        print("3. Exibir Saldo")
        print("4. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            valor = float(input("Digite o valor a ser depositado: R$"))
            conta.depositar(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
        elif opcao == 2:
            valor = float(input("Digite o valor a ser sacado: R$"))
            if conta.sacar(valor):
                print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente!")
        elif opcao == 3:
            print(f"Saldo atual: R$ {conta.exibir_saldo():.2f}")
        elif opcao == 4:
            print("Saindo do programa....")
            break
        else: 
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()