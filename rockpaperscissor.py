import random

#given options

    
options=["Rock", "Paper", "Scissor"]
user_choice = input("Choose any one from the following options: \n \
    Rock \n \
    Paper \n \
    Scissor \n")
computer_choice = random.choice(options)
print("your choise: " , user_choice)
print("computer choise: " , computer_choice)
if user_choice == computer_choice:
    print("You both choose the same so game is tie!")
elif user_choice == "Rock" and computer_choice == "Scissor":
    print("You are the winner!")
elif user_choice == "Paper" and computer_choice == "Rock":
    print("You are the winner!")
elif user_choice == "Scissor" and computer_choice == "Paper":
    print("You are the winner")
else:
    print("computer wins better luck next time!")
    