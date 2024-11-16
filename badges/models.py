from django.db import models

# Create your models here.
class Badge(models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name