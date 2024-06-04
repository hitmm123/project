from django.db import models


class Food(models.Model):
    pid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, unique=True)
    price = models.IntegerField(null=False)

    def __str__(self):
        return self.name


class Deliveryi(models.Model):
    BRANCH = [(1, "khrebat al-souq"), (2, "yadoudeh"), (3, "zezia"), (4, "madaba")]
    bid = models.AutoField(primary_key=True)
    phonenumber=models.IntegerField
    adress = models.CharField(max_length=200, null=False)
    name = models.CharField(max_length=200, null=False)
    branch = models.IntegerField(choices=BRANCH, null=False)
    food = models.ForeignKey(Food, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name
