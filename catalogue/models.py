from django.db import models
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200, blank=True)
    image = models.ImageField(blank=True)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    name = models.CharField(max_length=200, blank=True)
    category = models.ForeignKey(
        Category, related_name="equipments", on_delete=models.CASCADE)
    availability = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Images(models.Model):
    image = models.ImageField(blank=True)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)

    def __str__(self):
        return self.equipment.name


