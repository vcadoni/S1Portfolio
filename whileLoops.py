#simple calculator
#While Loops
#only want to loop under certain conditions

#ex 1
#i = 0
#while i < 10:
     #print('i is' + str(i))#This is not good. this will make an infinite loop and overrun ur whole computer and it will blow up!!!!
     #i = i + 1 #do this to stop the loop once it becomes 10

#ex 2:
#while True: #Forever loop
    #print('This will loop forever')
    #break


#Init


#Funcs
#Adds two numbers together and prints the result
def add(num1,num2):
    result = num1+num2
    print(result)
def subtract(num1,num2):
    result = num1-num2
    print(result)
def multiply(num1,num2):
    result = num1*num2
    print(result)
def divide(num1,num2):
    result = num1/num2
    print(result)

def simpleCalc():
    print ("Welcome to Simple Calculator!")
    while True:
        print("Please select a mathematical operation:")
        print("""
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. Quit""")
        global add #will make operation functions available in the simpleCalc function
        global subtract
        global multiply
        global divide
        operation = int(input("(1-5) Option: "))
        if operation == 1: #adds
            int1 = int(input("Enter the first number: "))
            int2 = int(input("Enter the second number: "))
            add(int1,int2)
        if operation == 2: #subtracts
            int1 = int(input("Enter the first number: "))
            int2 = int(input("Enter the second number: "))
            subtract(int1,int2)
        if operation == 3: #multiplies
            int1 = int(input("Enter the first number: "))
            int2 = int(input("Enter the second number: "))
            multiply(int1,int2)
        if operation == 4: #divides
            int1 = int(input("Enter the first number: "))
            int2 = int(input("Enter the first number: "))
            divide(int1,int2)
        if operation == 5: #stops calculator
            print("Thank you for using the simple calculator!")
            break

#Main
simpleCalc()
