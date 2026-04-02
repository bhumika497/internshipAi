class Student_Record:
    def __init__(self, student_name, student_caste, student_roll):
        self.student_name = student_name
        self.student_caste = student_caste
        self.student_roll = student_roll

    def student_grade(self):
        sid = int(input("Enter student roll: "))
        student = next((x for x in student_details if x.student_roll == sid), None)
        if student:
            grade = input("Enter grade: ")
            print("Grade added successfully")
            return (student, grade)
        else:
            print("Student not found")
            return None


class Course:
    def __init__(self, course_id, course_name):
        self.course_id = course_id
        self.course_name = course_name

    def student_enrollment(self):
        sid = int(input("Enter student roll: "))
        cid = int(input("Enter course id: "))

        student = next((x for x in student_details if x.student_roll == sid), None)
        course = next((x for x in course_details if x.course_id == cid), None)

        if student and course:
            print("Student enrolled successfully")
            return (student, course)
        else:
            print("Incorrect data")
            return None


class Teacher_details:
    def __init__(self, teacher_name, teacher_id):
        self.teacher_name = teacher_name
        self.teacher_id = teacher_id


# Lists
student_details = []
course_details = []
teacher_details = []
student_enrollment = []
student_grades = []


# Functions (since no staticmethod)
def create_student():
    name = input("Enter name: ")
    caste = input("Enter caste: ")
    roll = int(input("Enter roll: "))
    print("Student created successfully")
    return Student_Record(name, caste, roll)


def create_course():
    cid = int(input("Enter course id: "))
    name = input("Enter course name: ")
    print("Course created successfully")
    return Course(cid, name)


def create_teacher():
    name = input("Enter teacher name: ")
    tid = int(input("Enter teacher id: "))
    print("Teacher created successfully")
    return Teacher_details(name, tid)


def display_all():
    print("\nStudents:")
    for s in student_details:
        print(s.student_name, s.student_caste, s.student_roll)

    print("\nCourses:")
    for c in course_details:
        print(c.course_id, c.course_name)

    print("\nTeachers:")
    for t in teacher_details:
        print(t.teacher_name, t.teacher_id)

    print("\nEnrollments:")
    for s, c in student_enrollment:
        print(s.student_name, "->", c.course_name)

    print("\nGrades:")
    for s, g in student_grades:
        print(s.student_name, ":", g)


# Main loop
while True:
    choice = int(input("""
1 for student
2 for course
3 for enrollment
4 for grade
5 for teacher
6 for display
7 for logout
Enter choice: """))

    if choice == 1:
        student = create_student()
        student_details.append(student)

    elif choice == 2:
        course = create_course()
        course_details.append(course)

    elif choice == 3:
        c = Course(0, "")
        enroll = c.student_enrollment()
        if enroll:
            student_enrollment.append(enroll)

    elif choice == 4:
        s = Student_Record("", "", 0)
        grade = s.student_grade()
        if grade:
            student_grades.append(grade)

    elif choice == 5:
        teacher = create_teacher()
        teacher_details.append(teacher)

    elif choice == 6:
        display_all()

    elif choice == 7:
        print("Logout successful")
        break

    else:
        print("Invalid choice")