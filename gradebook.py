import uuid
from enum import Enum


class AliveStatus(Enum):
    DECEASED = 0
    ALIVE = 1

class Person:
    def __init__(self, first_name, last_name, dob, alive):
        self.is_alive = alive

    def update_first_name(self, first_name):
        pass

    def update_last_name(self, last_name):
        pass

    def update_dob(self, dob):
        pass

    def update_status(self, alive):
        pass


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
        self.students = students
        self.instructors = instructors


    def add_instructor(self):
        pass


    def remove_instructor(self):
        pass


    def print_instructors(self):
        print()


    def print_students(self):
        print()

if __name__ == "__main__":
    is_alive = AliveStatus.ALIVE
    bob = Person("bob", "johnson", "today", is_alive)
