from departamento import Departamento

class Universidade:
    def __init__(self, nome):
        self.nome = nome
        self.departamentos = []

    def adicionar_departamento(self, departamento):
        if departamento not in self.departamentos:
            self.departamentos.append(departamento)
        else:
            print(f"O departamento '{departamento.nome}' já está vinculado à universidade.")

    def remover_departamento(self, departamento):
        if departamento in self.departamentos:
            departamento.remover_todos_professores()
            self.departamentos.remove(departamento)
        else:
            print(f"O departamento '{departamento.nome}' não está nesta universidade.")

    def remover_todos_departamentos(self):
        for departamento in list(self.departamentos):
            self.remover_departamento(departamento)

    def listar_departamentos(self):
        return [dep.nome for dep in self.departamentos]
