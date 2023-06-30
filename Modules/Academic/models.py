from django.db import models


# Create your models here.

class Career(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField(default=5)


class Student(models.Model):
    dni = models.CharField(max_length=8, primary_key=True)
    paternal_surname = models.CharField(max_length=35)
    maternal_surname = models.CharField(max_length=35)
    names = models.CharField(max_length=35)
    born_date = models.DateField()
    genres = [
        ('F', 'Feminine'),
        ('M', 'Masculine')
    ]
    genre = models.CharField(max_length=1, choices=genres, default='F')
    career = models.ForeignKey(Career, null=False, blank=False, on_delete=models.CASCADE)
    vigency = models.BooleanField(default=True)

    def get_full_name(self):
        full_name = {"{0} {1}, {2}"}
        return full_name.format(self.maternal_surname, self.paternal_surname, self.names)


class Course(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.PositiveSmallIntegerField()
    teacher = models.CharField(max_length=100)


class Enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now=True)