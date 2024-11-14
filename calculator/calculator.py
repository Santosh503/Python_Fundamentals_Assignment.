from math import sin,cos

class arithmetic:
    def add(a,b):
        return a+b
    def sub(a,b):
        return a-b
    def mul(a,b):
        return a*b
    def div(a,b):
        try:
            return a/b
        except ZeroDivisionError:
            print("The number is not divisible by zero")

class scientific(arithmetic):
    def sine(a):
        return sin(a)
    def cosine(a):
        return cos(a)
