# A simple game to random guess the number
import random

def random_number_guesser():
    Turns = 0
    random_number = random.randint(1,10)
    print("Random Number is generated!")
    while True:      
        player_value = int(input("Enter the Value and get it wrong Muhahaha! :"))
        if player_value == random_number:
            Turns = Turns + 1
            print(f"Congratulations on getting it right on the {Turns} attempts")
            return False
        else:
            Turns = Turns + 1
            print("Try again muhahahah!")
            pass


random_number_guesser()


