from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from todo_app.managers import Active


class Todo(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    deleted = models.IntegerField(default=0)
    done = models.BooleanField(default=False)

    # managers
    objects = models.Manager()
    active = Active()

    class Meta:
        db_table = 'todo'
