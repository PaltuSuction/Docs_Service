from django.db import models

# Create your models here.
from Docs_Service import settings


class Person(models.Model):
    userPerson = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True)
    lastName = models.CharField(max_length=50, verbose_name='Фамилия', help_text='Фамилия')
    firstName = models.CharField(max_length=50, verbose_name='Имя', help_text='Имя')
    middleName = models.CharField(max_length=50, null=True, blank=True, verbose_name='Отчество',
                                  help_text='Отчество (если есть)')
    #TODO: Это поле можно удалить
    email = models.EmailField(verbose_name='Email', help_text='Email', null=True, blank=True)

    class Meta:
        abstract = True


class Student(Person):
    #studentPhoto = models.ImageField(upload_to='media/profiles/student_profile_pics', null=True, blank=True)
    studentGroup = models.ForeignKey('Group', on_delete=models.CASCADE, verbose_name='Группа')
    ticketNumber = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'
        abstract = False

    def __str__(self):
        return 'Студент: {} {} {}'.format(self.lastName, self.firstName, self.middleName)


class Teacher(Person):
    #teacherPhoto = models.ImageField(upload_to='media/profiles/teacher_profile_pics', null=True, blank=True)
    teacherPhoneNumber = models.CharField(max_length=20, verbose_name='Номер телефона преподавателя', help_text='Номер телефона предподавателя', null=True, blank=True)
    departments = models.ManyToManyField('Department', verbose_name='Кафедры', help_text='Кафедры')

    class Meta:
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'
        abstract = False

    def __str__(self):
        return 'Преподаватель: {} {} {}'.format(self.lastName, self.firstName, self.middleName)


class Group(models.Model):
    number = models.CharField(max_length=4, verbose_name='Номер группы', help_text='Введите номер группы', unique=True)
    headman = models.OneToOneField('Student', verbose_name='Староста', help_text='Староста группы',
                                   null=True, blank=True, on_delete=models.SET_NULL)
    department = models.ForeignKey('Department', null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return 'Группа: {}'.format(self.number)


class Department(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название кафедры', help_text='Название кафедры', unique=True)
    faculty = models.ForeignKey('Faculty', null=True, blank = True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'

    def __str__(self):
        return 'Кафедра: {}'.format(self.name)


class Faculty(models.Model):
    name = models.CharField(max_length=300, verbose_name='Факультет', help_text='Факультет', unique=True)

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'

    def __str__(self):
        return 'Факультет: {}'.format(self.name)


class Discipline(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название дисциплины', help_text='Название дисциплины')
    teachers = models.ManyToManyField(Teacher, verbose_name='Преподаватели', help_text='Преподаватели с этой дисциплиной')
    groups = models.ManyToManyField(Group, verbose_name='Группы', help_text='Группы с этой дисциплиной')

    class Meta:
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'

    def __str__(self):
        return 'Дисциплина: {}'.format(self.name)

