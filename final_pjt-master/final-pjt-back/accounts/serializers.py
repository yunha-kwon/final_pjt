from rest_framework import serializers
from django.contrib.auth import get_user_model
from dj_rest_auth.serializers import UserDetailsSerializer, TokenSerializer, TokenModel, LoginSerializer
from dj_rest_auth.registration.serializers import RegisterSerializer

class CustomRegisterSerializer(RegisterSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email', 'password1', 'password2']

class CustomUserDetailSerializer(UserDetailsSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'username', 'email',
                  'is_active', 'is_staff', 'is_superuser']
        read_only_fields = ['id']


class CustomTokenSerializer(TokenSerializer):
    user = CustomUserDetailSerializer(read_only=True)

    class Meta:
        model = TokenModel
        fields = ['key', 'user',]


class CustomLoginSerializer(LoginSerializer):
    username = serializers.CharField(required=False, allow_blank=True)
    # email = serializers.EmailField(required=False)
    email = None
    password = serializers.CharField(style={'input_type': 'password'})