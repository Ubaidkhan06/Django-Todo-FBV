from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=155)
    description = models.CharField(max_length=155)
    completed = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
        