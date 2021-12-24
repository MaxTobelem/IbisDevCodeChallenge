from rest_framework.serializers import ModelSerializer
 
from .models import Profile
 
class UserSerializer(ModelSerializer):
 
    class Meta:
        model = Profile
        fields = ['name','email','phone']