def analyze_students(students: list):
    if not isinstance(students,list):
        return {
            'status': False,
            'error': 'Data must be list',
            'data': None
        }
    total = 0
    passed = []
    topper_mark = float('-inf')
    topper = None

    for data in students:
        if not isinstance(data,dict):
            return {
            'status': False,
            'error': 'Student data must be in dict.',
            'data': None
        }
        req = {'name','marks'}
        if not req.issubset(data.keys()):
            return {
            'status': False,
            'error': 'Missing required fields.',
            'data': None
        }
        name = data.get('name')
        if not isinstance(name,str):
            return{
            'status': False,
            'error': 'Name must be in string',
            'data': None
        }
        mark = data.get('marks')
        if not isinstance(mark,int):
            return {
            'status': False,
            'error': 'Mark must be Integer',
            'data': None
        }
        if mark>=50:
            passed.append(name)
            if mark>topper_mark:
                topper_mark =mark
                topper =name
        total += mark
    average =round(total/len(students),2)
    return {
            'status': True,
            'Message': 'Student Analyzed ',
            'data': {
                'passed': passed,
                'topper': topper,
                'class Average': average
            }
        }
print(analyze_students(students = [
    {"name": "A", "marks": 85},
    {"name": "B", "marks": 40},
    {"name": "C", "marks": 72},
    {"name": "D", "marks": 33}
]
))