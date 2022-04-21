class Fraction:
    def __init__(self, n, d):
        self.num = n
        self.denom = d
        if self.denom < 0:
            self.denom = abs(self.denom)
            self.num = -1 * self.num
        elif self.denom == 0:
            raise ZeroDivisionError

    def Add(self, other):
        return self.num * other.denom + self.denom * other.num, self.denom * other.denom

    def Sub(self, other):
        return self.num * other.denom - self.denom * other.num, self.denom * other.denom

    def Mul(self, other):
        return self.num * other.num, self.denom * other.denom

    def Div(self, other):
        return self.num * other.denom, self.denom * other.num

    def Show(self):
        if self.denom % self.num:
            return self.num / (self.denom//self.num), self.denom / (self.denom//self.num)