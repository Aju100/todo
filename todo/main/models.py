from django.db import models

class YourTask(models.Model):
    title = models.CharField(max_length = 250)
    completed = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title