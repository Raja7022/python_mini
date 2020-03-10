import random 
def guess_number():
    x=random.randint(1,100)
    
    while True:
        user=int(input("guess a number between "))         
        if user==x:
            print("ola u guessed correctly ")
            break
        elif user>x:
            print("guess lesser than that")
        elif user<x:
            print("guess higher than that")


guess_number()                     