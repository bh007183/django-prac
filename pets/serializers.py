from curses import meta
from rest_framework import serializers
from .models import UserProfile, Pet

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['id', "phone_number"]
class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ["id", "species", "user"]