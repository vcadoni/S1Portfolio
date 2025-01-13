print ("Welcome to the Number Guesser Game!")
print("Guess a number from 1 to 10 to win the game! You have two tries...guess carefully!")

import random
#Functions
def rand_game():
    x = random.randint(1,10)
    ans = input("What do you think the number is? Enter a number 1-10")
    replay = input("Would you like to play again? Yes/No")
    if int(ans) == x:
        print("Congratulations! You guessed correctly that the number was " + str(x))
        print(replay)
        if replay == "Yes" or replay == "yes":
                rand_game()
    elif int(ans) < x:
        tooLow = input("Nice try, but you guessed wrong! The correct number is greater than " + str(ans) + ". You have one more guess. Please enter another number 1-10")
        tooLow
    elif int(ans) > x:
        tooHigh = input("Nice try, but you guessed wrong! The correct number is less than " + str(ans) + ". You have one more guess. Please enter another number 1-10")
        tooHigh
        if int(tooLow) == x or int(tooHigh) == x:
            print("Congratulations! You guessed correctly that the number was " + str(x))
        else:
            print("Sorry that was also not the answer, but don't lose hope!" + replay)
            if replay == "Yes" or replay == "yes":
                rand_game()
    else:
        print("Thanks for playing, we hope you play again!")

rand_game()

