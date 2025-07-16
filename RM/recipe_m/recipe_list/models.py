from django.db import models

# Create your models here.
class homePage(models.Model):
    recipe=models.CharField(max_length=20)
    ingredients=models.CharField(max_length=200)
    instructions=models.TextField()

    def __str__(self):
        return self.recipe


