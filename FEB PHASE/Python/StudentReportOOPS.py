class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_average(self):
        total = 0
        for mark in self.marks:
            total += mark
        return round(total / len(self.marks), 2)

    def get_result(self):
        avg = self.calculate_average()
        return "Passed" if avg >= 50 else "Failed"

    def display(self):
        avg = self.calculate_average()
        result = self.get_result()
        return f"Name: {self.name}\nAverage: {avg:.2f}\nResult: {result}"


std1 = Student('Raghav', [90, 99, 76])
print(std1.display())