from django.shortcuts import render
from django.core.serializers import serialize
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import CourseService, EnrollmentService
import json

@csrf_exempt
def get_courses(request):
    courses = CourseService.get_courses()
    return JsonResponse([course.__dict__ for course in courses], safe=False)

@csrf_exempt
def create_course(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        course = CourseService.create_course(**data)
        serialized_course = serialize('json', [course])
        return JsonResponse(json.loads(serialized_course)[0]['fields'], status=201)

@csrf_exempt
def enroll_student(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        student_name = data.get('student_name')
        course_id = data.get('course_id')
        is_valid, message = EnrollmentService.validate_enrollment(student_name, course_id)
        if not is_valid:
            return JsonResponse({"error": message}, status=400)
        enrollment = EnrollmentService.enroll_student(student_name, course_id)
        serialized_enrollment = serialize('json', [enrollment])
        return JsonResponse(json.loads(serialized_enrollment)[0], status=201)