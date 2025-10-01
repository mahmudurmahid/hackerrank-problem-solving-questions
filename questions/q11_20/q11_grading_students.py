import math

def grading_students(grades):
    final_grades = []

    for grade in grades:
        if grade < 38:
            final_grades.append(grade)
        else: # grade > 38
            rounded_grade = 5 * math.ceil(grade / 5)
            if rounded_grade - grade < 3:
                grade = rounded_grade
            else: # rounded grade - grade >= 3
                grade = grade
            final_grades.append(grade)
    
    return final_grades

grades_arr = [4, 73, 67, 38, 33]
result = grading_students(grades_arr)
print(result)