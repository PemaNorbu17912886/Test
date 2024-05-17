class Person:
    def __init__(self, name, age, cid):
        self.name = name
        self.age = age
        self.cid = cid
    def walk(self):
        print(f"{self.name} is walking.")
    
    def talk(self):
        print(f"{self.name} is talking.")
    
    def eat(self):
        print(f"{self.name} is eating.")
    
    def sleep(self):
        print(f"{self.name} is sleeping.")

class Teacher(Person):
    def __init__(self, name, age, cid, subject, salary, department, designation):
        super().__init__(name, age, cid)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation
    
    def teach(self):
        print(f"{self.name} is teaching {self.subject}.")
    
    def grade_students(self):
        print(f"{self.name} is grading students.")
    
    def attend_meeting(self):
        print(f"{self.name} is attending a meeting.")

class Student(Person):
    def __init__(self, name, age, cid, student_id, course, year, gpa):
        super().__init__(name, age, cid)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.gpa = gpa
    
    def study(self):
        print(f"{self.name} is studying.")
    
    def attend_class(self):
        print(f"{self.name} is attending class.")
    
    def write_exam(self):
        print(f"{self.name} is writing an exam.")


teacher = Teacher("Mr. Pema", 40, "CID1160400666", "Mathematics", 700000, "CSF101", "Senior Lecturer")
student = Student("MR. Norbu", 20, "CID1160400888", "STU123", "Computer Science", 2, 3.5)

                                    
teacher.walk()
teacher.talk()
teacher.teach()

student.walk()
student.talk()
student.study()
    