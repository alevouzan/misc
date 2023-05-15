from django.db import models

# Create your models here.


class Subscription(models.Model):
	name = "Sp Subscription"
	price = models.IntegerField(1000) #cents 1000=10$

	def  __str__(self):
		return self.price