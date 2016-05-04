from django.db import models
from django.contrib.auth.models import User

class Person(models.Model):
	matriculation = models.PositiveIntegerField() 			
	locker_password = models.CharField(max_length=50)
	RFID = models.CharField(max_length=200)

	def __str__(self):
		return self.matriculation


class Admin(Person):
	user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, blank=True)

class Locker(models.Model):
	locker_id = models.CharField(max_length=50)
	room = models.CharField(max_length=200, default="")

class Access(models.Model):
	person = models.ForeignKey('Person', on_delete=models.CASCADE)
	locker = models.ForeignKey('Locker', on_delete=models.CASCADE)
	initial_time = models.TimeField()
	final_time = models.TimeField()
