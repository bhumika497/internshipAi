class student_record:
    def __init__(self, student_id, name, address, roll_no):
        self.student_id = student_id
        self.name = name
        self.address = address
        self.roll_no = roll_no


class teacher:
    def __init__(self, teacher_id, name, course):
        self.teacher_id = teacher_id
        self.name = name
        self.course = course


class courses:
    def __init__(self, teacher_id, course_name):
        self.teacher_id = teacher_id
        self.course_name = course_name


class enrollment:
    def __init__(self, enrollment_id, enrollment_name, enrollment_course, year, semester):
        self.enrollment_id = enrollment_id
        self.enrollment_name = enrollment_name
        self.enrollment_course = enrollment_course
        self.year = year
        self.semester = semester


class grade:
    def __init__(self, grade_id, student_id, attendance):
        self.grade_id = grade_id
        self.student_id = student_id
        self.attendance = attendance


students = []
teachers = []
course_list = []
enrollments = []
grades = []


def add_student():
    sid = int(input("Enter student id: "))
    name = input("Enter name: ")
    address = input("Enter address: ")
    roll = input("Enter roll no: ")
    s = student_record(sid, name, address, roll)
    students.append(s)
    print("Student added successfully!")


def add_teacher():
    tid = int(input("Enter teacher id: "))
    name = input("Enter teacher name: ")
    course = input("Enter course: ")
    t = teacher(tid, name, course)
    teachers.append(t)
    print("Teacher added successfully!")


def add_course():
    tid = int(input("Enter teacher id: "))
    cname = input("Enter course name: ")
    c = courses(tid, cname)
    course_list.append(c)
    print("Course added successfully!")


def enroll_student():
    eid = int(input("Enter enrollment id: "))
    name = input("Enter student name: ")
    course = input("Enter course name: ")
    year = input("Enter year: ")
    semester = input("Enter semester: ")
    e = enrollment(eid, name, course, year, semester)
    enrollments.append(e)
    print("Enrollment successful!")


def add_grade():
    gid = int(input("Enter grade id: "))
    sid = int(input("Enter student id: "))
    attendance = input("Enter attendance: ")
    g = grade(gid, sid, attendance)
    grades.append(g)
    print("Grade added successfully!")


def display_all():
    print("\nStudents:")
    for s in students:
        print(s.student_id, s.name, s.address, s.roll_no)

    print("\nTeachers:")
    for t in teachers:
        print(t.teacher_id, t.name, t.course)

    print("\nCourses:")
    for c in course_list:
        print(c.teacher_id, c.course_name)

    print("\nEnrollments:")
    for e in enrollments:
        print(e.enrollment_id, e.enrollment_name, e.enrollment_course, e.year, e.semester)

    print("\nGrades:")
    for g in grades:
        print(g.grade_id, g.student_id, g.attendance)


def logout():
    print("\nLogging out... Goodbye!")
    exit()


while True:
    choice = int(input(
        "\n1 for student\n2 for teacher\n3 for course\n4 for enrollment\n5 for grade\n6 for display\n7 for logout\nEnter a choice: "
    ))

    if choice == 1:
        add_student()
    elif choice == 2:
        add_teacher()
    elif choice == 3:
        add_course()
    elif choice == 4:
        enroll_student()
    elif choice == 5:
        add_grade()
    elif choice == 6:
        display_all()
    elif choice == 7:
        logout()
    else:
        print("Invalid choice!")