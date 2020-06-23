from math import sqrt

def getPrimeDividers(n):
    number = n
    dividers = []
    i = 2
    count = 0
    while i <= number:
        count+=1
        if number % i == 0:
            dividers.append(i)
            number //= i
        else:
            i += 1
    print("Non opt iterations:", count)
    return dividers

def getPrimeDividersOpt(n):
    number = n
    dividers = []
    count = 0
    for i in range(2, int(sqrt(n))):
        while(number % i == 0):
            dividers.append(i)
            number //= i
            count += 1
    if number != 1:
        dividers.append(number)
    print("Opt iterations:", count)
    return dividers

def getMaxDividers(n, maxK= -1):
    dividers = []
    i = int(sqrt(n))
    while i > 0:
        if n % i == 0:
            K = (n//i) / i
            if K <= maxK or maxK == -1:
                dividers.append((n//i, i, K))
            else:
                break
        i -= 1

    return dividers


n = int(input())

maxK = 2

# for i in reversed(range(0, n)):


#print(getPrimeDividers(n))
#print(getPrimeDividersOpt(n))
print(getMaxDividers(n, maxK))
