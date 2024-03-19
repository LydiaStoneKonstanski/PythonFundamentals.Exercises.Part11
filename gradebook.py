import uuid
from enum import Enum


class AliveStatus(Enum):
    DECEASED = 0
    ALIVE = 1


class Person:
    def __init__(self, first_name, last_name, dob, alive):
        self.is_alive = alive
        self.first_name = first_name
        self.last_name = last_name
        self.dob = dob



    def update_first_name(self, first_name):
        self.first_name = first_name


    def update_last_name(self, last_name):
        self.last_name = last_name


    def update_dob(self, dob):
        self.dob = dob


    def update_status(self, alive):
        self.alive = alive


class Instructor(Person):
    def __init__(self, first_name, last_name, dob, alive):
        super().__init__(first_name, last_name, dob, alive)
        self.instructor_id = str(uuid.uuid4())
        print("Instructor" + self.instructor_id)


class Student(Person):
    def __init__(self, first_name, last_name, dob, alive):
        super().__init__(first_name, last_name, dob, alive)
        self.student_id = str(uuid.uuid4())
        print("Student" + self.student_id)


class ZipCodeStudent(Student):
    def __init__(self, first_name, last_name, dob, alive):
        super().__init__(first_name, last_name, dob, alive)


class ElementaryStudent(Student):
    def __init__(self, first_name, last_name, dob, alive):
        super().__init__(first_name, last_name, dob, alive)


class Classroom:
    def __init__(self, students, instructors):
        self.students = []
        self.instructors = []


    def add_instructor(self, instructor):
        self.instructors.append(instructor)


    def remove_instructor(self, instructor):
        self.instructors.remove(instructor)


    def print_instructors(self):
        print(self.instructors)


    def add_student(self, student):
        self.students.append(student)


    def remove_student(self, student):
        self.student.remove(student)


    def print_students(self):
        print(self.students)

if __name__ == "__main__":
    is_alive = AliveStatus.ALIVE
    bob = Person("bob", "johnson", "today", is_alive)
