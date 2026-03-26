def calculate_avg(marks):
    total = 0
    for mark in marks:
        total += mark
    total = total
    return round(total/len(marks),2)
def is_fail(avg):
    if avg<50:
        return f"Failed"
    return f"Passed"
def find_topper(students):
    topper = None
    topper_score = float("-inf")
    for student in students:
        if student['avg']> topper_score:
            topper = student
            topper_score = student['avg']
    return topper
def generate_report(students):
    with open("report.txt", 'w') as file:
        file.write("--- Student Report ---\n\n")

        for student in students:
            file.write(
                f"{student['name']:<10}- Avg: {student['avg']:.2f} - {student['result']}\n"
            )

        topper = find_topper(students)
        file.write(f"\nTopper: {topper['name']} ({topper['avg']:.2f})")

def main():
    students = [
    {"name": "Raghav", "marks": [78, 85, 90]},
    {"name": "Amit", "marks": [40, 35, 30]},
    {"name": "Neha", "marks": [88, 92, 84]},
    {"name": "Priya", "marks": [60, 70, 65]},
    {"name": "Karan", "marks": [33, 38, 40]}
    ]
    for student in students:
        student['avg'] = calculate_avg(student['marks'])
        student['result'] = is_fail(student['avg'])
    topper = find_topper(students)

    print(f"Topper -> {topper['name']}, Score: {topper['avg']}")
    name = input("Enter student name to see report: ").lower()
    found = 0
    for student in students:
        if name == student['name'].lower():
            print(f"{student['name']}'s REPORT:")
            print(f"Score: {student['avg']}")
            print(f"Result: {student['result']}")
            found = 1
    if found == 0:
        print("!!- No student Found -!!")
        
    generate_report(students)

if __name__== "__main__":
    main()