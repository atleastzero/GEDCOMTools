import re

import family
import person

class Builder:
    
    def __init__(self, gedcom):
        f=open(gedcom, "r")
        if f.mode == 'r':
            self.lines = f.read().splitlines()
        f.close()
        self.people = []
        self.families = {}
        self.loop()

    def print_lines(self):
        for line in self.lines:
            print(line)

    def loop(self):
        try:
            current_index = 0
            print(self.lines[current_index])
            while self.lines[current_index]:
                print("looking for person")
                if re.search("@P", self.lines[current_index]):
                    print("found a person")
                    person_id = re.findall(r"\d", self.lines[current_index])
                    current_index += 1
                    name = "NOT A NAME"
                    if re.search("NAME", self.lines[current_index]):
                        name = re.search(r"NAME [a-zA-Z\s/']+", self.lines[current_index]).group()[5:]
                    print(name)
                    data_dump = []
                    person_families = []
                    while not re.search("FAM", self.lines[current_index]):
                        data_dump.append(self.lines[current_index])
                        current_index += 1
                    print(data_dump)
                    while not re.search("@P", self.lines[current_index]):
                        if re.search("FAM", self.lines[current_index]):
                            family_id = int(re.search(r"\d", self.lines[current_index]).group())
                            print(type(family_id))
                            family = family.Family(family_id)
                            print(family)
                            person_families.append(family)
                            self.families[family_id] = family
                            print(family)
                        current_index += 1
                    person = person.Person(person_id, name, file_dump, families)
                    self.people.append(person)
                    current_index -= 1
                current_index += 1
        except:
            print("this file is empty")

    def print_people(self):
        for person in self.people:
            print(person)

def tests():
    obryans = Builder("Obryan.ged")
    # obryans.print_lines()
    obryans.print_people()

if __name__ == "__main__":
    tests()