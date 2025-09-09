student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60,
}

student_grades = {}

for keys, value in student_scores.items():
    if 91 <= value <= 100:
        student_grades[keys] = "Outstanding"
    elif 81 <= value <= 90:
        student_grades[keys] = "Exceeds Expectations"
    elif 71 <= value <= 80:
        student_grades[keys] = "Acceptable"
    else:
        student_grades[keys] = "Fail"

print(student_grades)
