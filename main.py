from university import University
from professor import Professor
from subject import Subject


def main():
    university = University("UEA")
    print(f"\nUniversity: {university.name}")

    university.create_departments()

    professor_names = [
        "Ciclano da Silva",
        "Beltrano de Souza",
        "Raimundo Nonato",
        "Girafales",
        "Brás Cubas",
    ]
    professors = [Professor(name) for name in professor_names]

    for dep, prof in zip(university.departments, professors):
        dep.add_professor(prof)

    print("\nDepartments:")
    for department in university.list_departments():
        print(f"- {department}")

    print("\nAdded Professors:")
    for dep in university.departments:
        print(f"{dep.name}: {dep.list_professors()}")

    subject_data = [
        ('Programação de Computadores e Algoritmos', 60),
        ("Cálculo 1", 90),
        ("Mecânica dos Sólidos", 66),
        ("Eletricidade", 66),
        ('Química Geral', 60),
    ]

    subjects = [
        Subject(name, workload, prof)
        for (name, workload), prof in zip(subject_data, professors)
    ]

    for prof, subj in zip(professors, subjects):
        prof.add_subject(subj)

    print("\nAdded Subjects:")
    for prof in professors:
        print(f"{prof.name}: {prof.list_subjects()}")

    print("\nSubject Details:")
    for subj in subjects:
        print(f"- {subj.subject_info()}")


if __name__ == "__main__":
    main()
