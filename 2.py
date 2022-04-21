class Time:
    def __init__(self, h, m, s):
        self.hour = h
        self.minute = m
        self.second = s

    def Add(self, other):
        s = self.second + other.second
        m = self.minute + other.minute
        h = self.hour + other.hour
        if s>60:
            s -= 60
            m += 1
        if m>60:
            m -= 60
            h += 1
        return h, m, s

    def Sub(self, other):
        s = self.second - other.second
        m = self.minute - other.minute
        h = self.hour - other.hour
        if s < 60:
            s += 60
            m -= 1
        if m < 60:
            m += 60
            h -= 1
        return h, m, s

    def Time2second(self):
        return self.hour * 3600 + self.minute * 60 + self.second

    def Second2time(self):
        return self.second // 3600, self.second - self.second // 60 * 60 - self.second // 3600 * 3600, self.second - self.second // 60 * 60
