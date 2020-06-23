from math import sqrt

from Resolution import Resolution


def getMaxDividers(n, maxK=-1.0):
    dividers = []
    i = int(sqrt(n))
    while i > 0:
        if n % i == 0:
            K = (n // i) / i
            if K <= maxK or maxK == -1:
                dividers.append(Resolution(n // i, i))
            else:
                break
        i -= 1

    return dividers


def getArgs(numOfArgs, allowedArgs, startMsg="Enter Options", errMsg="Wrong Args", argsMsgs=[]):
    def checkArg(args, allowedArgs):
        for i in args:
            if not (i in allowedArgs):
                return False
        return True

    args = [0] * numOfArgs
    if len(argsMsgs) == 0:
        argsMsgs = [""] * numOfArgs

    print(startMsg)
    for i in range(numOfArgs):
        if numOfArgs > 1: print(argsMsgs[i])
        args[i] = int(input())
    while (not checkArg(args, allowedArgs)):
        print(errMsg, startMsg)
        for i in range(numOfArgs):
            if numOfArgs > 1: print(argsMsgs[i])
            args[i] = int(input())
    return args



'''print("Select Mode:\n1) Square \n2) Sides")

mode = int(input())

while (mode != 1 and mode != 2):
    print("Wrong Option!")
    print("Select Mode:\n1) Square \n2) Screen sides")
    mode = int(input())

square = 0'''

'''if mode == 1:
    print("Enter square")
    square = int(input())
else:
    print("Enter \"A\" side")
    a = int(input())
    print("Enter \"B\" side")
    b = int(input())
    square = a * b
print("Enter max A/B ratio")

maxK = float(input())
'''

mode = getArgs(numOfArgs=1, allowedArgs = [1, 2], startMsg="Select Mode:\n1) Square \n2) Screen sides")[0]



print(mode)
#deviders = getMaxDividers(square, maxK)
"""for res in deviders:
    print(res.getString())"""
