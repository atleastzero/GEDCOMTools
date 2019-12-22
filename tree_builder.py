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
        self.loop_for_people()

    def print_lines(self):
        for line in self.lines:
            print(line)

    def loop_for_people(self):
        try:
            current_index = 0
            print(self.lines[current_index])
            while self.lines[current_index]:
                print("looking for person")
                if re.search("@P", self.lines[current_index]):
                    print("found a person")
                    current_index += 1
                    data = []
                    while not re.search("@P", self.lines[current_index]):
                        data.append(self.lines[current_index])
        except Exception as e:
            print(e)

    def print_people(self):
        for person in self.people:
            print(person)

def tests():
    obryans = Builder("Obryan.ged")
    # obryans.print_lines()
    obryans.print_people()

if __name__ == "__main__":
    tests()