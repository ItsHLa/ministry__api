from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from accounts.admin import create_get_group
from accounts.models import User


class SignUpSerializer(ModelSerializer):
    is_employee = serializers.BooleanField(required=True)
    class Meta:
        model = User
        fields = ('username', 'email','password','is_employee')
        
    
    def create(self,validated_data):
        user = User.objects.create_user(
            username  = validated_data['username'],
            email = validated_data['email'],
            password=validated_data['password']
        )
        if validated_data['is_employee']:
            (employee_group, created,) = create_get_group(name='employee')
            employee_group.user_set.add(user)
        refresh = RefreshToken.for_user(user)
        return {'message': 'account created successfully',
                'refresh_token': str(refresh),
                'access_token': str(refresh.access_token)}

class LoginSerializer(ModelSerializer):
    email = serializers.EmailField()
    class Meta:
        model = User
        fields = ('email','password')

    def check_user(self,email , password):
        email = email.lower()
        if not User.objects.filter(email=email).exists(): 
            return {'message': 'user dose not exists'}
        user = User.objects.get(email=email)
        if not user.check_password(password):
            return {'msg' : "error password dosent match"}
        refresh = RefreshToken.for_user(user)
        return {
                'msg': 'login successful',
                'access_token': str(refresh.access_token),
                'refresh_token': str(refresh),
                }    
        

class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

