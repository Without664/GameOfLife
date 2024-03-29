
from django.db import models

class Cell(models.Model):
    row = models.IntegerField()
    col = models.IntegerField()

    def __str__(self):
        return f"Cell({self.row}, {self.col})"