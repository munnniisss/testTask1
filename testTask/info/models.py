from django.db import models


class Info(models.Model):
    name_building = models.CharField(max_length=150)
    name_company = models.CharField(max_length=150)
    quarters = models.IntegerField()

    def __str__(self):
        return self.name_building
