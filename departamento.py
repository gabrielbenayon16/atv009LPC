class Departamento:
    def __init__(self, nome):
        self.nome = nome
        self.professores = []

    def adicionar_professor(self, professor):
        if len(self.professores) < 5:
            self.professores.append(professor)
        else:
            print("O departamento já atingiu o limite de 5 professores.")

    def listar_professores(self):
        return [p.nome for p in self.professores]
