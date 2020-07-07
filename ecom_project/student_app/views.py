from django.shortcuts import render
from .models import Student


# Create your views here.
def students(request):
    students = Student.objects.all()
    context = {'students': students}
    return render(request, 'student_app/students.html', context)


def student_details(request, id):
    student = Student.objects.get(id=id)
    context = {'std': student}
    return render(request, 'student_app/student_details.html', context)


# def student_details(request, roll):
#     students = {
#         1: {
#             'name': 'Std 1',
#             'gender': 'Male',
#             'phone': '242424'
#         },
#         2: {
#             'name': 'Std 2',
#             'gender': 'Female',
#             'phone': '242422'
#         },
#         3: {
#             'name': 'Std 3',
#             'gender': 'Male',
#             'phone': '242422'
#         },
#         4: {
#             'name': 'Std 5',
#             'gender': 'Male',
#             'phone': '242424'
#         },
#     }
#     student = students[roll]
#     context = {'std': student}
#     return render(request, 'student_app/student_details.html', context)
