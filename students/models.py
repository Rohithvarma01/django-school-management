from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    grade = models.CharField(max_length=10)
    contact = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.name} - Grade {self.grade}"
