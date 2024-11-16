from django.db import models

# Create your models here.
class Season(models.Model):
    month = models.PositiveIntegerField()

    def __str__(self):
        return self.month