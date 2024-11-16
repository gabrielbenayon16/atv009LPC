from disciplina import Disciplina

class Professor:
    def __init__(self, nome):
        self.nome = nome
        self.disciplinas = []

    def adicionar_disciplina(self, disciplina):
        if len(self.disciplinas) < 5:
            self.disciplinas.append(disciplina)
        else:
            print("O professor já atingiu o limite de 5 disciplinas.")

    def listar_disciplinas(self):
        return [d.nome for d in self.disciplinas]