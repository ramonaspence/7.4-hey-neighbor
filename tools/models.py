from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

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
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.name

# Create your models here.
