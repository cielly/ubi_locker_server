from rest_framework import serializers
from .models import Person, Admin

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('matriculation','locker_password')

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin