from rest_framework import serializers
from django.contrib.auth import get_user_model
from job_application_app.models import Profile

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'email', 'phone_number')

class RegisterSerializer(serializers.ModelSerializer):
    phone_number = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name'],
            password=validated_data['password']
        )
        Profile.objects.create(user=user, phone_number=validated_data['phone_number'])
        return user