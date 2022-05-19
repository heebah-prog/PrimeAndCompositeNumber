
def isNumberValid(num):
    if(num <= 1):
        return -1 // Number not Valid
    else:
        return num

# print(isNumberValid(1))

def primeChecker(num):
    isPrime = True
    for x in range(2,num):
        result = num%x
        if(result == 0):
            isPrime = False
            break
        else:
            isPrime = True

    print(isPrime)

# primeChecker(5)
