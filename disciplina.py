class Disciplina:
    def __init__(self, nome, carga_horaria, professor=None):
        self.nome = nome
        self.carga_horaria = carga_horaria
        self.professor = professor

    def informacoes_disciplina(self):
        return {
            "nome": self.nome,
            "carga_horaria": self.carga_horaria,
            "professor": self.professor.nome if self.professor else "Nenhum"
        }
