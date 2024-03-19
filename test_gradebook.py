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






