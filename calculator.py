# CLI Calculator
import math 
#Instructions for the calculator
# print("*****Calculator*****")
# print("-----------Instructions------------")
# print("+ for addition\n - for subtraction \n * for multiplication \n / for division ")
# print(" ** for power \n r for root \n ! for factorial \n sin for sine \n cos for cosine")

# print("Enter the operation you want to perform: ")
# operation = input().lower()
while True:
    print("**Calculator**")
    print("--Instructions--")
    print("+ for addition\n - for subtraction \n * for multiplication \n / for division ")
    print(" ** for power \n r for root \n ! for factorial \n sin for sine \n cos for cosine")

    print("Enter the operation you want to perform: ")
    operation = input().lower()

    # while (operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == "**" or operation == "r" or operation == "!" or operation == "sin" or operation == "cos") :

    if operation == "!" or operation == "sin" or operation == "cos":
        try:
            print("Enter the number: ")
            number = float(input())
            if operation == "sin":
                print("sine of ",number,"=",math.sin(number))
            elif operation == "cos":
                print("Cosine of ",number,"=",math.cos(number))
            elif operation == "!":
                temp = number
                temporary = 1
                while temp > 1:
                    temporary *= temp
                    temp -= 1
                print("Factorial of ",number, "is equal to ", temporary)
        except:
            print("Enter valid number")
    elif (operation == "+" or operation == "-" or operation == "*" or operation == "/" or operation == "**" or operation == "r") :
        try:
            print("Enter the first number: ")
            firstNumber = float(input())
            print("Enter the second number: ")
            secondNumber = float(input())
            if operation == "+":
                print(firstNumber,"+",secondNumber," = ",firstNumber + secondNumber)                    
            elif operation == "-":
                print(firstNumber,"-",secondNumber," = ",firstNumber - secondNumber)
            elif operation == "*":
                print(firstNumber,"*",secondNumber," = ",firstNumber * secondNumber)
            elif operation == "/":
                print(firstNumber,"/",secondNumber," = ",firstNumber / secondNumber)
            elif operation == "**":
                print(firstNumber,"power of ",secondNumber," = ",firstNumber ** secondNumber)
            elif operation == "r":
                print(firstNumber,"root of",secondNumber," = ",secondNumber ** 1/firstNumber)
        except:
            print("Enter valid number")
    else:
        print("Enter valid operator :)")
    continue
    #var = input("Enter 1 to continue: ")