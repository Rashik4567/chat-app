from rest_framework import serializers
from .models import profile, massage
from django.contrib.auth.models import User


class massageSerializer(serializers.ModelSerializer):
    class Meta:
        model = massage
        fields = '__all__'


class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = '__all__'


class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']


class userCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
