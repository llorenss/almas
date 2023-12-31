from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

class Address(models.Model):
    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    person = models.ForeignKey(Person, on_delete=models.CASCADE)

class Friendship(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="%(class)s_user")
    friend = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="%(class)s_friend")

class Price(models.Model):
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    price = models.FloatField()

class Car(models.Model):
    brand = models.CharField(max_length=100)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)