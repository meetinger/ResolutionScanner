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


def getArgs(numOfArgs, allowedArgs, startMsg="Enter value", errMsg="Invalid value!", argsMsgs=[], argType=int,
            mode="one_line"):
    def checkArg(args, allowedArgs):
        if isinstance(allowedArgs, list):
            for i in args:
                if not (argType(i) in allowedArgs):
                    return False
            return True
        else:
            for i in args:
                if not allowedArgs(argType(i)):
                    return False
            return True

    raw_args = []

    def getArg(i):
        nonlocal raw_args
        if mode == "line_by_line":
            return argType(input())
        if mode == "one_line":
            if (not raw_args) or (not checkArg(raw_args, allowedArgs)):
                raw_args = input().split(" ")
            return argType(raw_args[i])

    args = [0] * numOfArgs

    if not argsMsgs == 0:
        argsMsgs = [""] * numOfArgs

    '''
    print(startMsg)
    for i in range(numOfArgs):
        if numOfArgs > 1 and mode == "line_by_line":
            print(argsMsgs[i])
        args[i] = getArg(i)'''
    while (not checkArg(args, allowedArgs)):
        if raw_args:
            print(errMsg)
        print(startMsg)
        for i in range(numOfArgs):
            if numOfArgs > 1 and mode == "line_by_line":
                print(argsMsgs[i])
            args[i] = getArg(i)
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
    decreaserType = getArgs(numOfArgs=1, allowedArgs=[1, 2],
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


help_sorts_order = "Sorts order\nIf the items in the priority sort are equal, then the lower priority values ​​will be sorted by the lower priority sort.\n" \
                   "Add minus \"-\" to sort in descending order. \n" \
                   "For example:\n" \
                   "3 4 -2 -1\n" \
                   "These parameters will sort the results first by side A, then by side B, by aspect ratio (descending) and by area (descending)\n" \
                   "Options:" \
                   "\n1) Square(default)" \
                   "\n2) A/B ratio" \
                   "\n3) A side" \
                   "\n4) B side" \


sorts_order = getArgs(numOfArgs=4, allowedArgs=lambda x: -4 <= x <= 4 and x!=0, startMsg=help_sorts_order, mode="one_line")


comparators = [lambda res: res.getSquare(), lambda res: res.getK(), lambda res: res.getA(), lambda res: res.getB(),
               lambda res: -res.getB(), lambda res: -res.getA(), lambda res: -res.getK(), lambda res: -res.getSquare()]

def fix_index(x):
    if x > 0:
        return (x - 1)
    else:
        return x


sorts_order = list(map(fix_index, sorts_order))

for i in reversed(sorts_order):
    deviders.sort(key=comparators[i])


for res in deviders:
    print(res.getString())
