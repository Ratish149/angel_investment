from rest_framework import serializers
from .models import Company, CompanyTag, CompanyTeam, Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = ['id', 'full_name', 'email', 'role', 'organization_role', 'organization_name', 'organization_logo', 'organization_description',
                  'contact_number', 'website_link', 'document', 'investment_interest_area']


class CompanySmallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ['id', 'company_name', 'tags']


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
