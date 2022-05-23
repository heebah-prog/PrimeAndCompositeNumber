# Program to Calculate Prime Numbers and Composite Number
# Program Get input from user
# Then show how many iteration need to find out if number is Prime or not
# If number is not prime, it displays the factor(s) of given number

# Application Implement two methods
# Method1: regular calculation Method
# Method2: Use Algorithm

import math


def isInputValid(num):
    if(num <= 1):
        return -1
    else:
        return num

# print(isNumberValid(1))

def primeCheckerMethod1(num):
    isPrime = False
    iteration = 0

    if(num == 2): 
        isPrime = True
    for x in range(2,num):
        iteration += 1
        if(num%x == 0):
            isPrime = False
            break
        else:
            isPrime = True

    return isPrime, iteration

# Method 2 uses the Primality Test Algorithm
def primeCheckerMethod2(n):
    isPrime = False
    iteration2 = 0
    if n==1 or n==0 or (n%2 == 0 and n>2):
        return isPrime, iteration2
    else:
        for i in range(3, int(math.sqrt(n))+1,2):
            iteration2 += 1
            if(n%i) == 0:
                return isPrime, iteration2
        isPrime = True
        return isPrime, iteration2


def getFactorsOfCompositeNumber(num):
    factors= []
    for x in range(2, num):
        if(num%x == 0):
            factors.append(x)
        else:
            pass
    return factors

# ***************************************
#            APPLICATION ENTRY
# ***************************************


userInput = int(input("\nPlease give a number -> "))

isPrime, iteration = primeCheckerMethod1(userInput)
factors = getFactorsOfCompositeNumber(userInput)
isPrime2, iteration2 = primeCheckerMethod2(userInput)

if(isInputValid(userInput) != -1):
    if(isPrime == True):
        print("\n"+ str(userInput) +" is prime number and factors are -> 1,"+str(userInput))
        print("with 1st method number of iteration is: "+str(iteration))
        print("with 2nd method number of iteration is: "+str(iteration2) +"\n")
    else:
        factorsOfCompositeNumber = ', '.join(map(str,factors))
        print("\n"+ str(userInput)+" is a composite Number and factors are -> "+str(factorsOfCompositeNumber))
        print("with 1st Method number of iteration is: "+str(iteration))
        print("with 2nd Method number of iteration is: "+str(iteration2) + "\n")
else:
    print("Number should be in range of 2 and above")
