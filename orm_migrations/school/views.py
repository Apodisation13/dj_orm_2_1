from django.views.generic import ListView
# from django.shortcuts import render

from .models import Student


class StudentView(ListView):
    model = Student
    template_name = 'school/students_list.html'

    def get_queryset(self):
        return Student.objects.all().order_by('group').prefetch_related('teacher')

# def students_list(request):
#     template = 'school/students_list.html'
#
#     ordering = 'group'
#     students = Student.objects.all().order_by(ordering).prefetch_related('teacher')
#
#     context = {'object_list': students}
#
#     return render(request, template, context)
