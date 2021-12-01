from django.db import models


class Ph(models.Model):
    ph = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'[{self.pk}] {self.ph} :: {self.created_at}'
