from django.db import models

# Create your models here.


class Person(models.Model):
    firstName = models.CharField(max_length=150, verbose_name='Имя', help_text='Имя')
    lastName = models.CharField(max_length=150, verbose_name='Фамилия', help_text='Фамилия')
    middleName = models.CharField(max_length=150, null=True, blank=True, verbose_name='Отчество',
                                  help_text='Отчество (если есть)')
    email = models.EmailField(verbose_name='Email', help_text='Email', null=True, blank=True)

    class Meta:
        abstract = True


class Student(Person):
    studentPhoto = models.ImageField(upload_to='media/profiles/student_profile_pics', null=True, blank=True)
    studentGroup = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name='Группа')
    ticketNumber = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Студент'
        abstract = False


class Teacher(Person):
    teacherPhoto = models.ImageField(upload_to='media/profiles/teacher_profile_pics', null=True, blank=True)
    teacherPhoneNumber = models.IntegerField(verbose_name='Номер телефона преподавателя', help_text='Номер телефона предподавателя', null=True, blank=True)
    departments = models.ManyToManyField('Department', verbose_name='Кафедры', help_text='Кафедры')

    class Meta:
        verbose_name = 'Преподаватель'
        abstract = False


class Group(models.Model):
    number = models.CharField(max_length=4, verbose_name='Номер группы', help_text='Введите номер группы')
    headman = models.OneToOneField('Student', verbose_name='Староста', help_text='Староста группы',
                                   null=True, blank=True, on_delete=models.SET_NULL)
    department = models.ForeignKey('Department', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Группа'


class Department(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название кафедры', help_text='Название кафедры')
    faculty = models.ForeignKey('Faculty', null=True, blank = True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Кафедра'


class Faculty(models.Model):
    name = models.CharField(max_length=300, verbose_name='Факультет', help_text='Факультет')

    class Meta:
        verbose_name = 'Факультет'


class Discipline(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название дисциплины', help_text='Название дисциплины')
    teachers = models.ManyToManyField(Teacher, verbose_name='Преподаватели', help_text='Преподаватели с этой дисциплиной')
    groups = models.ManyToManyField(Group, verbose_name='Группы', help_text='Группы с этой дисциплиной')

    class Meta:
        verbose_name = 'Дисциплина'

