class Family:
    def __init__(self, family_id):
        self.family_id = family_id
        self.spouserents = []
        self.children = []
    
    def __str__(self):
        return "this family has id", self.family_id