from django.db import models

# Create your models here.


class Customer(models.Model):
    name=models.CharField(max_length=200)
    age=models.PositiveSmallIntegerField()

    def __str__(self) -> str:
        return self.name + str(self.age)
