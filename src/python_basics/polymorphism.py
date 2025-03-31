class Human:
    def __init__(self, name):
        self.name = name

    def whatsmyname(self):
        return self.name + " is my name and I'm Sanju's girlfriend!"
    
class pet:
    def __init__(self, name):
        self.name = name

    def whatsmyname(self):
        return self.name + " is my name and I'm Rhea's pet"
    
rhea = Human('Rhea')
maxu = pet('Maxu')
    
for identity in [rhea,maxu]:
    print(identity.whatsmyname())