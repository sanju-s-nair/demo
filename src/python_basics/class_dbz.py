class Character:

    def __init__(self,name,power_level,HP,Signature):
        print("A Dragon Ball Character is created!")
        self.name = name
        self.power_level = power_level
        self.HP = HP
        self.Signature = Signature

    def roster(self):
        return (f"Character Name: {self.name}\nPower Level: {self.power_level}\nHitpoints: {self.HP}\nSignature Move: {self.Signature}")

    def __str__(self):
        return (f"{self.name}")

vegeta = Character('Vegeta', 8999, 300, 'Final Flash')



print(str(vegeta))
