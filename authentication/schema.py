import graphene
from graphene_django.types import DjangoObjectType
from .models import CustomUser, Company, CompanyTag, CompanyTeam  # Import your models

class CustomUserType(DjangoObjectType):
    class Meta:
        model = CustomUser

class CompanyType(DjangoObjectType):
    class Meta:
        model = Company

class CompanyTagType(DjangoObjectType):
    class Meta:
        model = CompanyTag

class CompanyTeamType(DjangoObjectType):
    class Meta:
        model = CompanyTeam

class Query(graphene.ObjectType):
    custom_users = graphene.List(CustomUserType)
    companies = graphene.List(CompanyType)
    company_tags = graphene.List(CompanyTagType)
    company_teams = graphene.List(CompanyTeamType)

    # New query to get a CustomUser by ID
    custom_user = graphene.Field(CustomUserType, id=graphene.Int(required=True))
    
    # New query to get a Company by ID
    company = graphene.Field(CompanyType, id=graphene.Int(required=True))

    # New query to get a CompanyTag by ID
    company_tag = graphene.Field(CompanyTagType, id=graphene.Int(required=True))

    # New query to get a CompanyTeam by ID
    company_team = graphene.Field(CompanyTeamType, id=graphene.Int(required=True))

    def resolve_custom_users(self, info, **kwargs):
        return CustomUser.objects.all()

    def resolve_companies(self, info, **kwargs):
        return Company.objects.all()

    def resolve_company_tags(self, info, **kwargs):
        return CompanyTag.objects.all()

    def resolve_company_teams(self, info, **kwargs):
        return CompanyTeam.objects.all()

    # Resolver for fetching a CustomUser by ID
    def resolve_custom_user(self, info, id):
        return CustomUser.objects.get(pk=id)

    # Resolver for fetching a Company by ID
    def resolve_company(self, info, id):
        return Company.objects.get(pk=id)

    # Resolver for fetching a CompanyTag by ID
    def resolve_company_tag(self, info, id):
        return CompanyTag.objects.get(pk=id)

    # Resolver for fetching a CompanyTeam by ID
    def resolve_company_team(self, info, id):
        return CompanyTeam.objects.get(pk=id)

schema = graphene.Schema(query=Query)
