import re

class Person:
    def __init__(self, person_id, file_dump):
        self.person_id = person_id
        # self.name = ""
        self.data = file_dump
        self.families = []
        self.parse_dump()

    def parse_dump(self):
        for line in self.data:
            if re.search("NAME", line):
                try:
                    self.name = re.search(r"NAME [\w\s/'-]+", line).group()[5:]
                except:
                    self.name = "Unknown"
        if self.name == "":
            self.name = "Unknown"

    def __str__(self):
        return "Person with id " + str(self.person_id) + " is named " + str(self.name)