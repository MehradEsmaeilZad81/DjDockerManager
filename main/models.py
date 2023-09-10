from django.db import models

# Create your models here.


class App(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)
    envs = models.JSONField()
    command = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Run(models.Model):
    RUNNING = 'Running'
    FINISHED = 'Finished'

    STATUS_CHOICES = [
        (RUNNING, 'Running'),
        (FINISHED, 'Finished'),
    ]

    app = models.ForeignKey(App, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    parameters = models.JSONField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)

    def __str__(self):
        return f"Run of {self.app.name} ({self.start_time})"
