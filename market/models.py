from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# class Ticket(models.Model):
    
class Order(models.Model):
    type = models.CharField(max_length = 5, choices=[('buy', 'buying'), ('sell', 'selling')])
    game = models.CharField(max_length = 100, null = True)
    row = models.CharField(max_length = 10, default='any')
    section = models.CharField(max_length = 10, default='any')
    price = models.PositiveIntegerField()
    phone = models.CharField(max_length = 50, null=True)
    status = models.CharField(max_length = 5, choices=[('s', 'satisfied'), ('w', 'waiting'), ('a', 'available')], default = 'a')
    reject_counter = models.PositiveIntegerField(default = 0)
    views = models.PositiveIntegerField(default = 0)
    

