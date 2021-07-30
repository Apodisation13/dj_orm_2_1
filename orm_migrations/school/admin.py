from django.contrib import admin

from .models import Student, Teacher


class ThroughInline(admin.TabularInline):
    model = Student.teacher.through


@admin.register(Student)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ThroughInline]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
