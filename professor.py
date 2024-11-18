class Professor:
    def __init__(self, name):
        self.name = name
        self.subjects = []
        self.department = None

    def add_subject(self, subject):
        if subject not in self.subjects:
            self.subjects.append(subject)
            subject.professor = self

    def remove_subject(self, subject):
        if subject in self.subjects:
            subject.professor = None
            self.subjects.remove(subject)

    def remove_all_subjects(self):
        for subject in list(self.subjects):
            self.remove_subject(subject)

    def list_subjects(self):
        return [subj.name for subj in self.subjects]
