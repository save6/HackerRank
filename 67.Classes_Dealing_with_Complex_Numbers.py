import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.init_real = real
        self.init_imaginary = imaginary
        self.real = real
        self.imaginary = imaginary
        
        
    def __add__(self, no):
        self.real = self.init_real + no.init_real
        self.imaginary = self.init_imaginary + no.init_imaginary
        return self.__str__()
        
    def __sub__(self, no):
        self.real = self.init_real - no.init_real
        self.imaginary = self.init_imaginary - no.init_imaginary
        return self.__str__()
        
    def __mul__(self, no):
        self.real = (self.init_real * no.init_real) - (self.init_imaginary * no.init_imaginary)
        self.imaginary = (self.init_real * no.init_imaginary) + (self.init_imaginary * no.init_real)
        return self.__str__()

    def __truediv__(self, no):
        r1 = (self.init_real * no.init_real) + (self.init_imaginary * no.init_imaginary)
        i1 = (self.init_real * no.init_imaginary * -1) + (self.init_imaginary * no.init_real)
        r2 = no.init_real * no.init_real
        i2 = no.init_imaginary * no.init_imaginary
        v2 = r2 + i2
        self.real = r1 / v2
        self.imaginary = i1 / v2
        return self.__str__()

    def mod(self):
        self.real = math.sqrt(self.init_real**2 + self.init_imaginary**2)
        self.imaginary = 0
        return self.__str__()
    
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')