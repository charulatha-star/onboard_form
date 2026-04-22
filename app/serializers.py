from rest_framework import serializers
from .models import Client, SignIn


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'



class SignInSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignIn
        fields = '__all__'