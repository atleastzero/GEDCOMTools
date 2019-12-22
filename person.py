class Person:
    def __init__(self, person_id, file_dump):
        self.person_id = person_id
        self.name = "NOT A NAME"
        self.data = file_dump
        self.families = []

    def __str__(self):
        return "Person with id " + str(self.person_id) + " is named " + str(self.name)