from django.db import models


class Craft(models.Model):
    name = models.TextField(max_length=32)
    origin = models.TextField(max_length=30)


class Astronaut(models.Model):
    craft = models.ForeignKey(Craft, on_delete=models.CASCADE)
    age = models.IntegerField()
    name = models.TextField(max_length=26)
    time_in_space = models.IntegerField()
