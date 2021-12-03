from django.db import models


class Arduino(models.Model):
    ph = models.FloatField()
    temperature = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.pk}] (ph = {self.ph}, T = {self.temperature}) :: {self.created_at}'
