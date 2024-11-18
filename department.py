class Department:
    def __init__(self, name):
        self.name = name
        self.professors = []

    def add_professor(self, professor):
        if professor not in self.professors:
            self.professors.append(professor)
            professor.department = self

    def remove_professor(self, professor):
        if professor in self.professors:
            professor.department = None
            self.professors.remove(professor)

    def remove_all_professors(self):
        for professor in list(self.professors):
            self.remove_professor(professor)

    def list_professors(self):
        return [prof.name for prof in self.professors]
