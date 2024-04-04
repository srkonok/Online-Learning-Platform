from .models import Course, Enrollment

class CourseService:
    @staticmethod
    def get_courses():
        return Course.objects.all()

    @staticmethod
    def create_course(title, description, instructor, duration, price):
        course = Course.objects.create(title=title, description=description, instructor=instructor, duration=duration, price=price)
        return course

    @staticmethod
    def get_course_by_id(course_id):
        return Course.objects.get(pk=course_id)

    @staticmethod
    def filter_courses(**kwargs):
        return Course.objects.filter(**kwargs)

class EnrollmentService:
    @staticmethod
    def enroll_student(student_name, course_id):
        enrollment = Enrollment.objects.create(student_name=student_name, course_id=course_id)
        return enrollment

    @staticmethod
    def validate_enrollment(student_name, course_id):
        course = Course.objects.filter(pk=course_id).exists()
        if not course:
            return False, "Course not found"
        return True, "Enrollment is valid"
