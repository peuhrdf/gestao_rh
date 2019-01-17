from django.db import models


class ResgistroHoraExtra(models.Model):
    motivo = models.CharField(max_length=100)


    def __str__(self):
        return self.motivo


