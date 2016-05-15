from rest_framework import serializers
from .models import Person, Admin, Locker
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff', 'password', 'is_active')

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('matriculation','locker_password')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin

class LockerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Locker        