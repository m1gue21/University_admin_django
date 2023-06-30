from django.db import models


# Create your models here.

class Career(models.Model):
    id = models.CharField(max_length=3, primary_key=True)
    name = models.CharField(max_length=50)
    duration = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        career_display_name = "{0}(Duration: {1} years)"
        return career_display_name.format(self.name, self.duration)


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
        full_name = "{0} {1}, {2}"
        return full_name.format(self.paternal_surname, self.maternal_surname, self.names)

    def __str__(self):
        display_text = "{0} / Career: {1} / {2}"
        if self.vigency:
            student_state = "Active"
        else:
            student_state = "Inactive"
        return display_text.format(self.get_full_name(), self.career, student_state)


class Course(models.Model):
    id = models.CharField(max_length=6, primary_key=True)
    name = models.CharField(max_length=30)
    credits = models.PositiveSmallIntegerField()
    teacher = models.CharField(max_length=100)

    def __str__(self):
        display_text = "{0} ({1}) / Teacher: {2}"
        return display_text.format(self.name, self.id, self.teacher)


class Enrollment(models.Model):
    id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, null=False, blank=False, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, null=False, blank=False, on_delete=models.CASCADE)
    enrollment_date = models.DateField(auto_now=True)

    def __str__(self):
        display_text = "{0} enrolled to the course {1} / Date: {2}"
        enrollment_date = self.enrollment_date.strftime("%A %d/%m/%Y %H:%M:%S")
        return display_text.format(self.student.get_full_name(), self.course, enrollment_date)
