from django.db import models
from django.utils import timezone

import datetime

# Create your models here.


class User(models.Model):
    user_name = models.CharField(max_length=200)
    def __str__(self):
        return self.user_name


class Input(models.Model):
    date = models.DateField()
    do = models.CharField(max_length=200)
    time = models.TimeField()
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    def __str__(self):
        return self.time
