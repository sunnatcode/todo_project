from django.contrib.auth.models import User
from django.db import models


class Employee(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    picture = models.IntegerField(null=False)

    class Meta:
        db_table = "auth_employee"
