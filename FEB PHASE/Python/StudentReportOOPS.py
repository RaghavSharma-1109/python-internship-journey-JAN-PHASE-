class Student:
    def __init__(self,name,marks:list) -> None:
        self.name = name
        self.marks = marks
    def calculate_average(self):
        sum = 0
        for mark in self.marks:
            sum += mark
        return round(sum/len(self.marks),2)
    def get_result(self):
        if Student.calculate_average(self) > 50:
            return 'Passed'
        return 'Failed'
    def display(self):
        avg = Student.calculate_average(self)
        result = Student.get_result(self)
 
        return( 
            f"""
            Name: {self.name}
            Average: {avg}
            Result : {result}""")
std1 = Student('Raghav', [90,99,76])
print(std1.display())