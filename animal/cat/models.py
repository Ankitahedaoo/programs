from django.db import models

# Create your models here.

class short(models.Model):
    url=models.CharField(max_length=100)
    alfanumeric=models.CharField(max_length=100)

    def __str__(self):
        return self.url