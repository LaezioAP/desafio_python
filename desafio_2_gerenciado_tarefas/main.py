class Tarefa:
    def __init__(self, titulo, descricao, status = "pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.status = status
    
    def concluir_tarefa(self):
        self.status = "concluida"


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
    
    def adicionar_tarefa(self, tarefa):
        self.tarefas.append(tarefa)

    def remover_tarefa(self, tarefa):
        self.tarefas.remove(tarefa)

    def concluir_tarefa(self, tarefa):

        for t in self.tarefas:
            if t.titulo == tarefa:
                t.concluir_tarefa()
                print(f"Tarefa '{t.titulo}' concluída com sucesso!")
                return
        print("Tarefa não encontrada!")

    def listar_tarefas(self):
        if not self.tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        for i, tarefa in enumerate(self.tarefas):
            print(f"{i + 1}. {tarefa.titulo.capitalize()} - {tarefa.status}")

def main():
    gerenciar = GerenciadorTarefas()

    while True: 
        print("\n Menu: ")
        print("1. Adicionar Tarefa")
        print("2. Remover Tarefa")
        print("3. listar Tarefas")
        print("4. Concluir Tarefa")
        print("5. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            titulo = input("Digite o título da tarefa: ").lower()
            descricao = input("Digite a descrição da tarefa: ")
            tarefa = Tarefa(titulo, descricao)
            gerenciar.adicionar_tarefa(tarefa)
            print(f"Tarefa '{titulo}' adicionada com sucesso!")
        elif opcao == 2:
            gerenciar.listar_tarefas()

            if not gerenciar.tarefas:
                continue

            indice = int(input("Digite o número da tarefa a ser removida: ")) - 1
            if 0 <= indice < len(gerenciar.tarefas):
                tarefa = gerenciar.tarefas[indice]
                gerenciar.remover_tarefa(tarefa)
                print(f"Tarefa '{tarefa.titulo}' removida com sucesso!")
            else:
                print("Tarefa inválida!")
        elif opcao == 3:
            gerenciar.listar_tarefas()
        elif opcao == 4:
            titulo = input("Digite o título da tarefa que deseja concluir: ").lower()
            gerenciar.concluir_tarefa(titulo)
        elif opcao == 5:
            print("Saindo do programa....")
            break
        else: 
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()