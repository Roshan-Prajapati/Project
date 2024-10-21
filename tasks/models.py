from django.db import models
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    status = models.BooleanField(default=False)  # False = Not Completed, True = Completed
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
