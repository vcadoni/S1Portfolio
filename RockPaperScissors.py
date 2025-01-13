#Victoria Adoni
#1/7/25
#Rock Paper Scissors

#Init
import random
wins = 0
losses = 0
ties = 0
#Functions
#Main

#Step 1: collect the player's move
print("""Welcome to the game of Rock, Paper, Scissors!
You will be playing against the robot named Bobby""")

#Step 4: Loop game until player wants to quit
while True:
    #Step 1: collect the player's move
    print("What is your move? Please capitalize the first letter:")
    player = input("Rock, Paper, Scissors, Shoot: ")
    print(player)

    #Step 2: generate Bobby's move
    bobby = random.randint(1,3)
    if bobby == 1:
        bobby = "Rock"
        print("Bobby played: Rock!")
    elif bobby == 2:
        bobby = "Paper"
        print("Bobby played: Paper!")
    else:
        bobby = "Scissors"
        print("Bobby played: Scissors!")

    #Step 3: Determine outcome
    if player == "Rock" and bobby == "Rock":
        print("You and Bobby have tied!")
        ties = ties + 1
        print("You have " + str(wins) + " wins, " + str(losses) + ' losses, and ' + str(ties) + " ties.") #Step 5:Keep track of the player's wins and losses
    elif player == "Rock" and bobby == "Paper":
        print("Sadly, Bobby won this round...")
        losses = losses + 1
        print("You have " + str(wins) + " wins, " + str(losses) + ' losses, and ' + str(ties) + " ties.")
    elif player == "Rock" and bobby == "Scissors":
        print("Congrats! You have won this round!")
        wins = wins + 1
        print("You have " + str(wins) + " wins, " + str(losses) + ' losses, and ' + str(ties) + " ties.")

    if player == "Paper" and bobby == "Rock":
        print("Congrats! You have won this round!")
        wins = wins + 1
        print("You have " + str(wins) + " wins, " + str(losses) + ' losses, and ' + str(ties) + " ties.")
    elif player == "Paper" and bobby == "Paper":
        print("You and Bobby have tied!")
        ties = ties + 1
        print("You have " + str(wins) + " wins, " + str(losses) + ' losses, and ' + str(ties) + " ties.")
    elif player == "Paper" and bobby == "Scissors":
        print("Sadly, Bobby won this round...")
        losses = losses + 1
        print("You have " + str(wins) + " wins, " + str(losses) + ' losses, and ' + str(ties) + " ties.")
    if player == "Scissors" and bobby == "Rock":
        print("Sadly, Bobby won this round...")
        losses = losses + 1
        print("You have " + str(wins) + " wins, " + str(losses) + ' losses, and ' + str(ties) + " ties.")
    elif player == "Scissors" and bobby == "Paper":
        print("Congrats! You have won this round!")
        wins = wins + 1
        print("You have " + str(wins) + " wins, " + str(losses) + ' losses, and ' + str(ties) + " ties.")
    elif player == "Scissors" and bobby == "Scissors":
        print("You and Bobby have tied!")
        ties = ties + 1
        print("You have " + str(wins) + " wins, " + str(losses) + ' losses, and ' + str(ties) + " ties.")
    #Step 4: Loop game until player wants to quit
    again = input("Would you like to keep playing? (Yes/No):")
    if again == "No":
        print("Thank you for playing")
        break



