from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token

class Person(models.Model):
	matriculation = models.PositiveIntegerField(primary_key=True) 			
	locker_password = models.CharField(max_length=50)
	RFID = models.CharField(max_length=200)

	def __str__(self):
		return self.matriculation

class Admin(Person):
	user = models.OneToOneField(User, on_delete=models.CASCADE, default=None, blank=True)
	pic = models.ImageField(upload_to="static/imgs/admin", default='static/imgs/admin/none.jpg')

	@receiver(post_save, sender=settings.AUTH_USER_MODEL)
	def create_auth_token(sender, instance=None, created=False, **kwargs):
		if created:
			Token.objects.create(user=instance) 

class Locker(models.Model):
	locker_id = models.CharField(max_length=50)
	room = models.CharField(max_length=200, default="")

class Access(models.Model):
	person = models.ForeignKey('Person', on_delete=models.CASCADE)
	locker = models.ForeignKey('Locker', on_delete=models.CASCADE)
	initial_time = models.TimeField(help_text="Please use the following format: <em>HH:MM</em>.")
	final_time = models.TimeField(help_text="Please use the following format: <em>HH:MM</em>.")

class Log(models.Model):
	person = models.ForeignKey('Person', on_delete=models.CASCADE)
	locker = models.ForeignKey('Locker', on_delete=models.CASCADE)
	time = models.DateTimeField()
	status = models.CharField(max_length=200)


