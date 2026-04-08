#Parte I
def initialize_dict(student_name, subject_grades):
    result = {student_name: subject_grades}
    return result

#P2
def add_student(student_grades= None):
    if student_grades == None:
        student_grades = {}
    Name = input("Enter student name: ")
    Name = Name.title()

    subjects = {}
    while True:
        Materias_Notas = input("Enter subject and grade (or 'exit' to finish): ")

        if Materias_Notas.lower() == "exit":
            break
        Subject, grade = Materias_Notas.split(",")
        Subject = Subject.title()
        grade = float(grade)

        subjects[Subject]= grade
    student_grades[Name]= subjects

    print(f"Student {Name} successfully added to the grades management system.")
    return student_grades

#P3
def get_students(student_grades, keys):
    result = {}
    for nombre in keys:
        counter =0
        for student in student_grades:
            if student.title() == nombre.title():
                result[student] = student_grades[student]
                counter = counter + 1
        if counter == 0:
            print(nombre.title(), "not found!")
    return result