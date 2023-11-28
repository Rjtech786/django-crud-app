from django.db import models


class Employees(models.Model):
    name = models.CharField(max_length=20)
    rollno = models.TextField(max_length=10)
    email = models.CharField(max_length=30)
    address = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)

    def __str__(self):
        return self.name
