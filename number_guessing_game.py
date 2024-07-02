import random

number = random.randint(1,10)
guess = None


while guess != number:
    guess = input ("guess a number between 1 and 10 : ")
    guess = int (guess)
    
    if guess == number:
        print("c0ngratulations ! you whin ")
    elif number >= guess:
        print ("this is the greater number than i guess")
    elif number <= guess:
        print ("this is too small than my guess")
    
    else:
        print("try Again!")