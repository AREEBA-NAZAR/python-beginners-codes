import random
name = input("enter your name: ")
print("hello", name ,"time to play game")
word = ("secret")
guesses = ""
No_of_turns = 10
print("you have ten numbers of turns")
while No_of_turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            print(char , end= "")
        else:
            print("_" , end="")
            failed += 1
    if failed == 0:
        print(" You won , CONGRULATION ",)
        break
    guess = input("guess a character: ")
    guesses += guess 
    if guess not in word:
        No_of_turns -=1
        print("wrong")
        print ("You have", + No_of_turns, 'more guesses' )
        if No_of_turns == 0:
            print("you lose")