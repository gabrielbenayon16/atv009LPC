from universidade import Universidade
from departamento import Departamento
from professor import Professor
from disciplina import Disciplina


def main():


    # criando a universidade
    universidade = Universidade("UEA")
    print(f"\nUniversidade: {universidade.nome}")


    # criando departamentos
    departamento1 = Departamento("Departamento de Ciclo Básico")
    departamento2 = Departamento("Departamento de Computação")
    departamento3 = Departamento("Departamento de Elétrica")
    departamento4 = Departamento("Departamento de Mecânica")
    departamento5 = Departamento("Departamento de Química")
    universidade.adicionar_departamento(departamento1)
    universidade.adicionar_departamento(departamento2)
    universidade.adicionar_departamento(departamento3)
    universidade.adicionar_departamento(departamento4)
    universidade.adicionar_departamento(departamento5)
    print("\nDepartamentos:")
    for departamento in universidade.listar_departamentos():
        print(f"- {departamento}")


    #Criando professores
    professor1 = Professor("Ciclano da Silva")
    professor2 = Professor("Beltrano de Souza")
    professor3 = Professor("Raimundo Nonato")
    professor4 = Professor("Girafales")
    professor5 = Professor("Brás Cubas")
    departamento1.adicionar_professor(professor1)
    departamento2.adicionar_professor(professor2)
    departamento3.adicionar_professor(professor3)
    departamento4.adicionar_professor(professor4)
    departamento5.adicionar_professor(professor5)
    print("\nProfessores adicionados:")
    print(f"Departamento {departamento1.nome}: {departamento1.listar_professores()}")
    print(f"Departamento {departamento2.nome}: {departamento2.listar_professores()}")
    print(f"Departamento {departamento3.nome}: {departamento3.listar_professores()}")
    print(f"Departamento {departamento4.nome}: {departamento4.listar_professores()}")
    print(f"Departamento {departamento5.nome}: {departamento5.listar_professores()}")


    #Criando disciplinas
    disciplina1 = Disciplina("Progrmação de Computadores e Algoritmos", 60, professor1)
    disciplina2 = Disciplina("Cálculo 1", 90, professor2)
    disciplina3 = Disciplina("Mecânica dos Sólidos", 66, professor3)
    disciplina4 = Disciplina("Probabilidade e Estatística", 66, professor4)
    disciplina5 = Disciplina("Química Geral", 60, professor5)
    professor1.adicionar_disciplina(disciplina1)
    professor2.adicionar_disciplina(disciplina2)
    professor3.adicionar_disciplina(disciplina3)
    professor4.adicionar_disciplina(disciplina4)
    professor5.adicionar_disciplina(disciplina5)
    print("\nDisciplinas adicionadas:")
    print(f"Professor {professor1.nome}: {professor1.listar_disciplinas()}")
    print(f"Professor {professor2.nome}: {professor2.listar_disciplinas()}")
    print(f"Professor {professor3.nome}: {professor3.listar_disciplinas()}")
    print(f"Professor {professor4.nome}: {professor4.listar_disciplinas()}")
    print(f"Professor {professor5.nome}: {professor5.listar_disciplinas()}")


    #Exibindo informações detalhadas
    print("\nDetalhes das Disciplinas:")
    print(f"- {disciplina1.informacoes_disciplina()}")
    print(f"- {disciplina2.informacoes_disciplina()}")
    print(f"- {disciplina3.informacoes_disciplina()}")
    print(f"- {disciplina4.informacoes_disciplina()}")
    print(f"- {disciplina5.informacoes_disciplina()}")

    # Finalizando
    print("\nSistema finalizado com sucesso!")

# executar o programa
if __name__ == "__main__":
    main()
