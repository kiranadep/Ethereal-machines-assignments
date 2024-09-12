from django.db import models

class Machine(models.Model):
    name = models.CharField(max_length=100)
    axis_x = models.FloatField()
    axis_y = models.FloatField()
    axis_z = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

