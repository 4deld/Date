from django.db import models

# Create your models here.
class Person(models.Model):
    username = models.CharField(max_length=200)
    def __str__(self):
        return self.username

class Info(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE) #user_id
    date = models.DateField()
    time = models.TimeField()
    do = models.CharField(max_length=200)
    def __str__(self):
        return self.do
