from django.db import models

class student(models.Model):
    name=models.CharField(max_length=25)
    email=models.EmailField()
    age=models.IntegerField()
    gender=models.CharField(max_length=25)

    def __str__(self):
        return self.name
