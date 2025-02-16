import graphene
from graphene_django.types import DjangoObjectType
from .models import CustomUser, Company, CompanyTag, CompanyTeam  # Import your models
from graphene_django_pagination import DjangoPaginationConnectionField

class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser

class CompanyType(DjangoObjectType):
    logo=graphene.String()
    class Meta:
        model = Company
        filter_fields = ['id']
    
    def resolve_logo(self, info):
        if self.logo:
            return self.logo.url
        return None    

class CompanyTagType(DjangoObjectType):
    class Meta:
        model = CompanyTag

class CompanyTeamType(DjangoObjectType):
    class Meta:
        model = CompanyTeam

class Query(graphene.ObjectType):
    custom_users = graphene.List(CustomUserType)
    companies = DjangoPaginationConnectionField(CompanyType)
    company_tags = graphene.List(CompanyTagType)
    company_teams = graphene.List(CompanyTeamType)


    def resolve_custom_users(self, info, **kwargs):
        return CustomUser.objects.all()

    def resolve_companies(self, info, **kwargs):
        return Company.objects.all()

    def resolve_company_tags(self, info, **kwargs):
        return CompanyTag.objects.all()

    def resolve_company_teams(self, info, **kwargs):
        return CompanyTeam.objects.all()


schema = graphene.Schema(query=Query)
