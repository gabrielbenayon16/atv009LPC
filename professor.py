from disciplina import Disciplina

class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []
        self.departamento = None

    def adicionar_disciplina(self, disciplina):
        if disciplina not in self.disciplinas:
            self.disciplinas.append(disciplina)
            disciplina.professor = self

    def remover_disciplina(self, disciplina):
        if disciplina in self.disciplinas:
            disciplina.professor = None
            self.disciplinas.remove(disciplina)

    def remover_todas_disciplinas(self):
        for disciplina in list(self.disciplinas):
            self.remover_disciplina(disciplina)

    def listar_disciplinas(self):
        return [disc.nome for disc in self.disciplinas]
