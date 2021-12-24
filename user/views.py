from django.shortcuts import render
from rest_framework.generics import CreateAPIView

from rest_framework.response import Response
from rest_framework import status

from .models import Profile
from .serializers import UserSerializer
 
#API PortfolioAPI
class Useriewset(CreateAPIView):
    serializer_class = UserSerializer
    queryset = Profile.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        user = Profile.objects.filter(email=request.data["email"])
        return Response({'id': user[0].id, 'createdAt' : user[0].createdAt}, status=status.HTTP_201_CREATED, headers=headers)

