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

# alternative solution
def alt_grading_students(grades):
    final_grades = []

    for grade in grades:
        if grade < 38:
            final_grades.append(grade)
        else:
            rounded_grade = 5 * math.ceil(grade / 5)
            if rounded_grade - grade < 3:
                final_grades.append(rounded_grade)
            else:
                final_grades.append(grade)

    return final_grades

grades_arr = [4, 73, 67, 38, 33]
result = grading_students(grades_arr)
print(result)
alt_result = alt_grading_students(grades_arr)
print(alt_result)