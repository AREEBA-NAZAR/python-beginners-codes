#fuction to define average marks:
def find_average_marks(marks):
    sum_of_marks=sum(marks)
    total_subjects=len(marks)
    average_marks=sum_of_marks / total_subjects
    return average_marks


#fuction to determine grades
def compute_grades(average_marks):
    if average_marks >=90:
        grade='A'
    elif average_marks >=70:
        grade='B'
    elif average_marks >=60:
        grade='C'
    else:
        grade='F'
    return grade
    

marks=[70,50,90,65,88]
average_marks=find_average_marks(marks)
print("average marks of s1 is:" ,average_marks)
grade=compute_grades(average_marks)
print("grade of s1 is:" , grade)

marks=[40,100,50,65,88]
average_marks=find_average_marks(marks)
print("average marks s2 is:" ,average_marks)
grade=compute_grades(average_marks)
print("grade of s2 is:" , grade)
