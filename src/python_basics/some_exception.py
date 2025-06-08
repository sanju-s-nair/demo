def askfornumber():
    while True:
        try:
            number = int(input("Please tell me your phone number!"))
        except:
            print("I literally asked you for a number :>")
            continue
        else:
            print("WOOHOO! thank you for your number, which is an integer ofcourse ;)")
            return "thats great my friend " + str(number) + " I'll save it"
    

print(askfornumber())