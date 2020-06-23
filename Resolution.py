class Resolution(object):
    '''def __init__(self, a, b, k, square):
        self.a = a
        self.b = b
        self.k = k
        self.square = square'''
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.k = a/b
        self.square = a*b

    def getA(self):
        return self.a

    def getB(self):
        return self.b

    def getK(self):
        return self.k

    def getSquare(self):
        return self.square

    def getString(self):
        res= str(self.a)+"x"+str(self.b)+" S="+str(self.square)+" K="+str(self.k)
        return res