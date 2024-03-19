from datetime import datetime
from unittest import TestCase
from unittest.mock import patch
from io import StringIO
import gradebook

class GradeBookTest(TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_create_instructor(self, stdout_mock):
        first_name = "Kris"
        last_name = "Younger"
        dob = datetime.now()
        is_alive = gradebook.AliveStatus.ALIVE

        instructor = gradebook.Instructor(first_name, last_name, dob, is_alive)

        self.assertEqual(first_name, instructor.first_name)
        self.assertEqual(last_name, instructor.last_name)
        self.assertEqual(dob, instructor.dob)
        self.assertEqual(is_alive, instructor.is_alive)
        self.assertTrue(isinstance(instructor.instructor_id, str))

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_student(self, stdout_mock):
        first_name = "Lydia"
        last_name = "Konstanski"
        dob = datetime.now()
        is_alive = gradebook.AliveStatus.ALIVE

        student = gradebook.Student(first_name, last_name, dob, is_alive)

        self.assertEqual(first_name, student.first_name)
        self.assertEqual(last_name, student.last_name)
        self.assertEqual(dob, student.dob)
        self.assertEqual(is_alive, student.is_alive)
        self.assertTrue(isinstance(student.student_id, str))

    @patch('sys.stdout', new_callable=StringIO)
    def test_create_classroom(self, stdout_mock):
        students = [
            gradebook.Student("Deepa", None, None, None),
            gradebook.Student("Nathan", None, None, None),
            gradebook.Student("Chris", None, None, None),
        ]
        instructors = [
            gradebook.Instructor("Kris", None, None, None)
        ]
        classroom = gradebook.Classroom(students, instructors)

        self.assertEqual(classroom.students, students)
        self.assertEqual(classroom.instructors, instructors)

    @patch('sys.stdout', new_callable=StringIO)
    def test_add_students(self, stdout_mock):
        deepa = gradebook.Student("Deepa", None, None, None)
        nathan = gradebook.Student("Nathan", None, None, None)

        students = [deepa]
        classroom = gradebook.Classroom(students, [])
        classroom.add_student(nathan)

        self.assertEqual(classroom.students, [deepa, nathan])

    @patch('sys.stdout', new_callable=StringIO)
    def test_add_instructor(self, stdout_mock):
        kris = gradebook.Instructor("Kris", None, None, None)
        dolio = gradebook.Instructor("Dolio", None, None, None)

        instructors = [kris]
        classroom = gradebook.Classroom([], instructors)
        classroom.add_instructor(dolio)

        self.assertEqual(classroom.instructors, [kris, dolio])


