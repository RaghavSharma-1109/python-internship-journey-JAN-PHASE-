import numpy as np

marks = np.array([
    [78, 85, 90],
    [40, 35, 30],
    [88, 92, 84],
    [60, 70, 65],
    [33, 38, 40]
])

# Average per student
avg_marks = np.mean(marks, axis=1)

# Topper
topper_index = np.argmax(avg_marks)
topper_score = avg_marks[topper_index]

print("Averages:", avg_marks)
print("Topper Index:", topper_index)
print("Topper Avg:", round(topper_score, 2))

# Subject-wise stats
print("Subject Mean:", np.mean(marks, axis=0))
print("Subject Max:", np.max(marks, axis=0))
print("Subject Min:", np.min(marks, axis=0))

# Top 3 students
top3 = np.argsort(avg_marks)[-3:][::-1]
print("Top 3 indices:", top3)