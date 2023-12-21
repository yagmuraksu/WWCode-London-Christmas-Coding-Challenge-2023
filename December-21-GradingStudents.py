def gradingStudents(grades):
    rounded_grades = []
    for i in range(len(grades)):
        rounded_grade = grades[i] + (5-(grades[i] % 5))

        if(grades[i] >= 38):
            if(rounded_grade - grades[i] < 3):
                new_grade = rounded_grade
            else:
                new_grade = grades[i]
        else:
            new_grade = grades[i]

        rounded_grades.append(new_grade)
    return rounded_grades
    
if __name__ == '__main__':

    grades = [73,67,38,33]

    result = gradingStudents(grades)

    print("Original grades:")
    print(grades)
    print("Final Grades")
    print(result)
