
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

