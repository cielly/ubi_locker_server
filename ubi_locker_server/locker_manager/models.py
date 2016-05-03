from django.db import models

class User(models.Model):
	name = models.CharField(max_length=200)
	matr = models.PositiveIntegerField(default=0) 	#matriculation
	email = models.EmailField(max_length=254)
	course = models.CharField(max_length=200)

	def __str__(self):
		return self.matriculation


# class Locker(models.Model):
# 	locker_id = models.CharField(max_length=50)
# 	admin = models.ManyToManyField(User)
