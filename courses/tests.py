from django.test import TestCase
from django.urls import reverse
from .services import CourseService, EnrollmentService

class CourseAPITest(TestCase):
    def setUp(self):
        self.course_data = {
            "title": "Python Programming",
            "description": "Learn Python programming language",
            "instructor": "John Doe",
            "duration": 60,
            "price": 49.99
        }

    def test_get_courses(self):
        response = self.client.get(reverse('get_courses'))
        self.assertEqual(response.status_code, 200)

    def test_create_course(self):
        response = self.client.post(reverse('create_course'), data=self.course_data, content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIn('title', response.json())

def test_enroll_student(self):
    enrollment_data = {
        "student_name": "Alice",
        "course_id": 1
    }
    response = self.client.post(reverse('enroll_student'), data=json.dumps(enrollment_data), content_type='application/json')
    self.assertEqual(response.status_code, 201)
    self.assertIn('student_name', response.json())


