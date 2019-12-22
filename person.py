class Person:
    def __init__(self, person_id, name, file_dump, families):
        self.person_id = person_id
        self.name = name
        self.data = file_dump
        self.families = []

    def __str__(self):
        return "Person with id " + str(self.person_id) + " is named " + str(self.name)