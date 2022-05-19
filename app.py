
def isInputValid(num):
    if(num <= 1):
        return -1
    else:
        return num

# print(isNumberValid(1))

def primeCheckerMethod1(num):
    isPrime = False
    iterationForPrime = 0

    for x in range(2,num):
        result = num%x
        iterationForPrime += 1
        if(result == 0):
            isPrime = False
            break
        else:
            isPrime = True

    return isPrime, iterationForPrime


def getFactorsOfCompositeNumber(num):
    factors= []
    iterationForComposite = 0
    for x in range(2, num):
        iterationForComposite +=1
        if(num%x == 0):
            factors.append(x)
        else:
            pass
    return factors, iterationForComposite



# ***************************************
#            APPLICATION ENTRY
# ***************************************

userInput = int(input("\nPlease give a number -> "))

isPrime, iterationForPrime = primeCheckerMethod1(userInput)
factors, iterationForComposite = getFactorsOfCompositeNumber(userInput)

if(isInputValid(userInput) != -1):
    if(isPrime == True):
        print("\n"+ str(userInput) +" is prime number and factors are -> 1,"+str(userInput))
        print("with 1st method number of iteration is: "+str(iterationForPrime) +"\n")
    else:
        factorsOfCompositeNumber = ', '.join(map(str,factors))
        print("\n"+ str(userInput)+" is a composite Number and factors are -> "+str(factorsOfCompositeNumber))
        print("with 1st Method number of iteration is: "+str(iterationForComposite) + "\n")
else:
    print("Number should be in range of 2 and above")
