# FizzBuzz -  A Simple program to implment FizzBuzz

def fizzbuzz(n):
    for i in range(1,n+1):
        if i%3==0 and i%5==0:
            print (f"{i} - FizzBuzz")
        elif i%3==0:
            print (f"{i} - Fizz")
        elif i%5==0:
            print (f"{i} - Buzz")
        else:
            pass

print(fizzbuzz(30))