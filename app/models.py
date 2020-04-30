from django.db import models

# Create your models here.
class Produto(models.Model):
    name = models.CharField(max_length=50, blank=False)
    quantity = models.CharField(max_length=5, blank=False)
    value = models.CharField(max_length=5, blank=False)

    def __str__(self):
        return self.name