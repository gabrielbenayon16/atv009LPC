from professor import Professor

class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        if professor not in self.professores:
            self.professores.append(professor)
            professor.departamento = self

    def remover_professor(self, professor):
        if professor in self.professores:
            professor.departamento = None
            self.professores.remove(professor)

    def remover_todos_professores(self):
        for professor in list(self.professores):
            self.remover_professor(professor)

    def listar_professores(self):
        return [prof.nome for prof in self.professores]
