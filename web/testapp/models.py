from django.db import models
import datetime
from django.contrib.auth.models import User


class Empmodel(models.Model):
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    # date = models.DateField(default=datetime.date.today)
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
