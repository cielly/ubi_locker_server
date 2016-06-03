from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from datetime import datetime, date


class Person(models.Model):
	matriculation = models.PositiveIntegerField(primary_key=True) 			
	locker_password = models.CharField(max_length=50, help_text='4-Digit password used to unlock the locker')
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

class Student(Person):
	program = models.CharField(default="", max_length=100)
	name = models.CharField(default="", max_length=200)		

class Locker(models.Model):
	locker_id = models.CharField(max_length=50)
	room = models.CharField(max_length=200, default="")

class Weekday(models.Model):
	WEEK_DAYS = (
		('1', 'segunda-feira'),
		('2', 'terca-feira'),
		('3', 'quarta-feira'),
		('4', 'quinta-feira'),
		('5', 'sexta-feira'),
		('6', 'sabado'),
		('7', 'domingo'),
	)	

	weekday = models.CharField(choices=WEEK_DAYS, max_length=50)

	def __str__(self):
		return self.get_weekday_display()

class Access(models.Model):
	person = models.ForeignKey('Person', on_delete=models.CASCADE)
	locker = models.ForeignKey('Locker', on_delete=models.CASCADE)
	initial_time = models.TimeField(help_text="Please use the following format: <em>HH:MM</em>.")
	final_time = models.TimeField(help_text="Please use the following format: <em>HH:MM</em>.")
	day = models.ManyToManyField(Weekday)

class Log(models.Model):
	person = models.ForeignKey('Person', on_delete=models.CASCADE)
	locker = models.ForeignKey('Locker', on_delete=models.CASCADE)
	time = models.DateTimeField()
	status = models.CharField(max_length=200)

	def __str__(self):
		return self.pk

	def register_success(self, access):
		self.locker = access.locker
		self.person = access.person
		self.time = datetime.now()
		self.status = "authorized"
		self.save()

	def register_failure(self, access):
		self.locker = access.locker
		self.person = access.person
		self.time = datetime.now()
		self.status = "denied"
		self.save()


