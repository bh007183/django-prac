from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import UserProfileSerializer, PetSerializer
from .models import UserProfile
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

from pets import serializers



# Create your views here.

class UserProfileViewSet(CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]

    # set detail to false if you want to see profile on list vew. if detail is true then you will see profile on detail view

    @action(detail = False, methods=['GET', 'PUT'])
   
    def me(self, request):
            (user, created) = UserProfile.objects.get_or_create(user_id=request.user.id)
            if request.method == 'GET':
                serializer = UserProfileSerializer(user)
                return Response(serializer.data)
            elif request.method == 'PUT':
                serializer = UserProfileSerializer(user, data = request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response(serializer.data)



    


