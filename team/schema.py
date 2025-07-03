import graphene
from graphene_django.types import DjangoObjectType
from .models import OurTeam, OurPartner
from graphene_django_pagination import DjangoPaginationConnectionField


# Define a GraphQL type for the OurTeam model
class OurTeamType(DjangoObjectType):
    class Meta:
        model = OurTeam
        filter_fields = ['id']

# Define a GraphQL type for the OurPartner model


class OurPartnerType(DjangoObjectType):
    class Meta:
        model = OurPartner
        filter_fields = ['id']

# Define a query to list all team members


class Query(graphene.ObjectType):
    all_team_members = DjangoPaginationConnectionField(OurTeamType)
    all_our_partners = DjangoPaginationConnectionField(OurPartnerType)

    def resolve_all_team_members(self, info, **kwargs):
        return OurTeam.objects.filter(**kwargs)

    def resolve_all_our_partners(self, info, **kwargs):
        return OurPartner.objects.filter(**kwargs)


# Create the schema
schema = graphene.Schema(query=Query)
