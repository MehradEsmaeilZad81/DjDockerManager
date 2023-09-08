from django.db import models

# Create your models here.


class App(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    envs = models.JSONField()
    command = models.CharField(max_length=255)

    def __str__(self):
        return self.name
