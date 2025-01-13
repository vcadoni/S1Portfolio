#Victoria
#1/9/25

#init
import random #step 2
print("""Welcome to the multiplication quiz!
We will give you two numbers to multiply and if you get the answer right, you win!
The quiz is 5 questions long. Let's get started""") #Step 1

#func
score = 0
#main
while True:
    global score
    for i in range(5): #loop to make the quiz 5 questions long
        num1 = random.randint(1,12) #step 2: generate random factors
        num2 = random.randint(1,12) #int
        print("The first factor is " + str(num1) + " and the other is " + str(num2)) #string
        guess = input("What do you think is " + str(num1) + " x " + str(num2) + " ?") #asking user for their answer
        answer = num1 * num2
        if guess == str(answer): #seeing if the user is correct
            print("Good job! " + str(answer) + " was the right answer.")
            score = score + 1 #updating score
            print("You have gotten the answer right " + str(score) + " out of 5 times this game!")
        else:
            print("Sorry but the answer was " + str(answer))
            print("You have gotten the answer right " + str(score) + " out of 5 times this game")
    print("Good effort! Your final score for this quiz was " + str(score/5 * 100) + "%") #telling user final score in a percentage
    again = input("Would you like to do another quiz?")
    if again == "No" or "no":
        print("Thank you for taking the quiz!")
        break

