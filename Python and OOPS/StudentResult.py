from ast import Return
from os import makedirs


class Student():
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def AverageMarks(self):
        sum =0
        number =0
        for i in self.marks:
            sum += i
            number += 1
        average = sum / number
        return average
    def is_passed(self):
        avg = self.AverageMarks()
        if  avg >= 40:
            return True
        else:
            return False
marks = [90, 89, 97,92,78]
student1 = Student('Raghav',marks)
result = Student.is_passed(student1)
print(result)
