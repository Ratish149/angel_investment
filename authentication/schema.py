import graphene
from graphene_django.types import DjangoObjectType
from .models import CustomUser, Company, CompanyTag, CompanyTeam  # Import your models
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

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

class CreateCustomUser(graphene.Mutation):
    class Arguments:
        email = graphene.String(required=True)
        password = graphene.String(required=True)
        role = graphene.String(required=True)
        photo = graphene.String()

    custom_user = graphene.Field(CustomUserType)

    def mutate(self, info, email, password, role, photo=None):
        if CustomUser.objects.filter(email=email).exists():
            raise Exception('This email is already in use.')  # Use a generic exception for GraphQL

        # Create user instance
        user = CustomUser(username=email, email=email, role=role, photo=photo)
        user.set_password(password)  # Hash the password
        user.is_active = False  # Keep inactive until verified
        user.save()

        # Send activation email using the class name
        CreateCustomUser.send_activation_email(user)

        return CreateCustomUser(custom_user=user)

    @staticmethod
    def send_activation_email(user):
        activation_link = f"http://127.0.0.1:8000/api/activate/{user.id}/"

        subject = "Activate Your Angel Investment Account"
        html_message = render_to_string("activation_email.html", {"user": user, "activation_link": activation_link})
        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            settings.EMAIL_HOST_USER,
            [user.email],
            html_message=html_message,
        )

class CreateCompany(graphene.Mutation):
    class Arguments:
        user_id = graphene.Int(required=True)
        company_id = graphene.Int()  # Optional argument for updating
        company_name = graphene.String(required=True)
        tags = graphene.List(graphene.Int)
        logo = graphene.String()
        trade_name = graphene.String()
        tagline = graphene.String()
        stage = graphene.String()
        contact_city = graphene.String()
        contact_country = graphene.String()
        contact_phone_number = graphene.String()
        contact_email = graphene.String()
        website = graphene.String()
        amount_raising = graphene.String()
        affiliation = graphene.String()
        company_description = graphene.String()

    company = graphene.Field(CompanyType)

    def mutate(self, info, user_id, company_name, company_id=None, tags=None, logo=None, trade_name=None, tagline=None,
               stage=None, contact_city=None, contact_country=None, contact_phone_number=None, contact_email=None,
               website=None, amount_raising=None, affiliation=None, company_description=None):
        user = CustomUser.objects.get(pk=user_id)
        
        if company_id:  # Update existing company
            company = Company.objects.get(pk=company_id)
            company.user = user
            company.company_name = company_name
            company.logo = logo
            company.trade_name = trade_name
            company.tagline = tagline
            company.stage = stage
            company.contact_city = contact_city
            company.contact_country = contact_country
            company.contact_phone_number = contact_phone_number
            company.contact_email = contact_email
            company.website = website
            company.amount_raising = amount_raising
            company.affiliation = affiliation
            company.company_description = company_description
            company.save()
        else:  # Create new company
            company = Company(user=user, company_name=company_name, logo=logo, trade_name=trade_name,
                              tagline=tagline, stage=stage, contact_city=contact_city,
                              contact_country=contact_country, contact_phone_number=contact_phone_number,
                              contact_email=contact_email, website=website, amount_raising=amount_raising,
                              affiliation=affiliation, company_description=company_description)
            company.save()

        if tags:
            company.tags.set(tags)  # Set many-to-many relationship
        return CreateCompany(company=company)

class CreateCompanyTag(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)

    company_tag = graphene.Field(CompanyTagType)

    def mutate(self, info, name):
        company_tag = CompanyTag(name=name)
        company_tag.save()
        return CreateCompanyTag(company_tag=company_tag)

class CreateCompanyTeam(graphene.Mutation):
    class Arguments:
        name = graphene.String(required=True)
        profile_picture = graphene.String()
        bio = graphene.String()
        position = graphene.String()
        linkedin = graphene.String()

    company_team = graphene.Field(CompanyTeamType)

    def mutate(self, info, name, profile_picture=None, bio=None, position=None, linkedin=None):
        company_team = CompanyTeam(name=name, profile_picture=profile_picture, bio=bio, position=position, linkedin=linkedin)
        company_team.save()
        return CreateCompanyTeam(company_team=company_team)

class Mutation(graphene.ObjectType):
    create_custom_user = CreateCustomUser.Field()
    create_company = CreateCompany.Field()
    create_company_tag = CreateCompanyTag.Field()
    create_company_team = CreateCompanyTeam.Field()

schema = graphene.Schema(query=Query, mutation=Mutation)
