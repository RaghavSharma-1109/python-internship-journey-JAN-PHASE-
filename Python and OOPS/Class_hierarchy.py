class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def get_info(self):
        return f"Name: {self.name}, Age: {self.age}"

class Student(Person):
    def __init__(self, name, age, marks):
        super().__init__(name, age)
        self.MARKS = marks
    def Average(self):
        total = 0
        for i in self.MARKS:
            total += i
        return total/len(self.MARKS)
    def get_info(self):
        avg = self.Average()
        return f'{super().get_info()}, Average Marks:{avg}'
    def is_passed(self):
        return self.Average()>=40
std_1 = Student('Raghav',20, [90,80,99,93])
print(std_1.is_passed())