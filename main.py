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


def getArgs(numOfArgs, allowedArgs, startMsg="Enter value", errMsg="Invalid value!", argsMsgs=[], argType=int):
    def checkArg(args, allowedArgs):
        if isinstance(allowedArgs, list):
            for i in args:
                if not (i in allowedArgs):
                    return False
            return True
        else:
            for i in args:
                if not allowedArgs(i):
                    return False
            return True

    def getArg():
        return argType(input())

    args = [0] * numOfArgs
    if len(argsMsgs) == 0:
        argsMsgs = [""] * numOfArgs

    print(startMsg)
    for i in range(numOfArgs):
        if numOfArgs > 1: print(argsMsgs[i])
        args[i] = getArg()
    while (not checkArg(args, allowedArgs)):
        print(errMsg, startMsg)
        for i in range(numOfArgs):
            if numOfArgs > 1: print(argsMsgs[i])
            args[i] = getArg()
    return args


dataType = getArgs(numOfArgs=1, allowedArgs=[1, 2], startMsg="Enter the data type:\n1) Square \n2) Screen sides")[0]

square = 0
if dataType == 1:
    square = getArgs(numOfArgs=1, allowedArgs=lambda x: x > 0, startMsg="Enter the square:")[0]
else:
    a = getArgs(numOfArgs=1, allowedArgs=lambda x: x > 0, startMsg="Enter the \"A\" side:")[0]
    b = getArgs(numOfArgs=1, allowedArgs=lambda x: x > 0, startMsg="Enter the \"B\" side:")[0]
    square = a * b

maxK = getArgs(numOfArgs=1, allowedArgs=lambda x: x > 0, startMsg="Enter the max A/B ratio:", argType=float)[0]

lowerResFind = getArgs(numOfArgs=1, allowedArgs=[1, 2], startMsg="Enable the lower resolution search?\n1) Yes \n2) No")[
    0]

threshold = 0
if lowerResFind == 1:
    # maxResDecrease = getArgs(numOfArgs=1, allowedArgs = lambda x: x > 1, startMsg="Enter the max Resolution decrease(how many times ) ")[0]
    decreaserType = getArgs(numOfArgs=1, allowedArgs=lambda x: [1, 2],
                            startMsg="Enter the type of decrasing threshold:\n1) Devider(how many times the new resolution may be less than the previous)"
                                     "\n2) Min resolution(Minimum threshold for new resolution)")[0]

    if decreaserType == 1:
        threshold = square // getArgs(numOfArgs=1, allowedArgs=lambda x: x > 0, startMsg="Enter the devider:")[0]
    else:
        threshold = getArgs(numOfArgs=1, allowedArgs=lambda x: x > 0, startMsg="Enter the min resolustion:")[0]

    step = getArgs(numOfArgs=1, allowedArgs=lambda x: x > 0, startMsg="Enter the step of decreasing(default=1):")[0]
else:
    threshold = square

i = square
deviders = []
while (i >= threshold):
    deviders += getMaxDividers(i, maxK)
    i -= 1

mainSort = getArgs(numOfArgs=1, allowedArgs=lambda x: [1, 4],
                   startMsg="Sort by:\n1) Square(default)"
                            "\n2) A/B ratio"
                            "\n3) A side"
                            "\n4) B side")[0] - 1

'''mainIsReverse = getArgs(numOfArgs=1, allowedArgs=lambda x: [1, 2],
                        startMsg="Sort:\n1) Ascending"
                              "\n2) Descending")[0]-1

secondSort = getArgs(numOfArgs=1, allowedArgs=lambda x: [1, 4],
                 startMsg="Sort by:\n1) Square(default)"
                          "\n2) A/B ratio"
                          "\n3) A side"
                          "\n4) B side")[0]'''

comparators = [lambda res: res.getSquare(), lambda res: res.getK(), lambda res: res.getA(), lambda res: res.getB(),
               lambda res: -res.getSquare(), lambda res: -res.getK(), lambda res: -res.getA(), lambda res: -res.getB()]

for res in reversed(sorted(deviders, key=comparators[mainSort])):
    print(res.getString())

# print(dataType)
# deviders = getMaxDividers(square, maxK)
"""for res in deviders:
    print(res.getString())"""
