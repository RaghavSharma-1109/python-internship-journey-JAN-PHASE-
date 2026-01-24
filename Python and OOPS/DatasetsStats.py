from math import sqrt
from statistics import variance


class DatasetStats:
    def __init__(self, data):
        self.data = data
    def mean(self):
        total = 0
        count = 0
        for i in self.data:
            total += i

        return total / len(self.data)
    def variance(self):
        mean = self.mean()
        sum =0
        for i in self.data:
            r = i - mean
            sum += r*r
        return sum / len(self.data)
    def Std_Variance(self):
        return sqrt(variance())
    def summary(self):
        print(f' Count   :{len(self.data)}')
        print(f' Variance :{(self.variance())}')
        print(f' Mean   :{(self.mean())}')

data = [10, 12, 14, 16, 18]
stats = DatasetStats(data)
stats.summary()

        