from django.contrib import admin
from core_part.models import Student, Teacher, Group, Department, Faculty, Discipline

# Register your models here.

#admin.site.register(Student)
@admin.register(Student)
class AdminStudent(admin.ModelAdmin):
    #fields = ('lastName', 'firstName', 'middleName', 'ticketNumber')
    ordering = ('lastName', 'firstName', 'middleName')

admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Department)
admin.site.register(Faculty)
admin.site.register(Discipline)