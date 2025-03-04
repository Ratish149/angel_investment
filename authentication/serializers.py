from rest_framework import serializers
from .models import CustomUser, Company, CompanyTag, CompanyTeam, Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'full_name', 'email', 'role', 'organization_name','organization_logo', 'organization_description', 
                 'contact_number', 'about_you', 'website_link', 'document']
    
class CustomUserSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'full_name','email', 'role', 'password', 'confirm_password']

    def validate(self, data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError("The passwords do not match.")
        return data

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['email'],
            email=validated_data['email'],
            password=validated_data['password'],
            full_name=validated_data['full_name'],
            role=validated_data['role']
        )
        return user

class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()

class VerifyLoginCodeSerializer(serializers.Serializer):
    email = serializers.EmailField()
    code = serializers.CharField()

class CompanySmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id','company_name', 'tags']

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyTag
        fields = '__all__'

class CompanyTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyTeam
        fields = '__all__'
