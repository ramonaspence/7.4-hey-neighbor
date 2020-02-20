from django.db import models

class Tool(models.Model):
    powertool = 'powertool'
    lawntool = 'lawntool'
    gardentool = 'gardentool'

    available_types = [
        (powertool, 'powertool'),
        (lawntool, 'lawntool'),
        (gardentool, 'gardentool'),
    ]

    name = models.CharField(max_length = 255)
    type = models.TextField(max_length = 255, choices = available_types)
    description = models.TextField(max_length = 255)
    borrowed = models.BooleanField()
    owner = models.CharField(max_length = 255) ##foreign key

    def __str__(self):
        return self.name

# Create your models here.
