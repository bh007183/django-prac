from dataclasses import fields
from djoser.serializers import UserCreateSerializer as BaseUserCreate

from djoser.serializers import UserSerializer as BaseUser

class UserCreateSerializer(BaseUserCreate):
    class Meta(BaseUserCreate.Meta):
        fields = ['id', 'username', 'password', 'email', 'first_name', 'last_name']

class UserSerializer(BaseUser):
    class Meta(BaseUser.Meta):
        fields = ["id", "email", "username", "first_name", "last_name"]
