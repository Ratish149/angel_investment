import graphene
from graphene_django.types import DjangoObjectType
from .models import OurTeam
from graphene_django_pagination import DjangoPaginationConnectionField


# Define a GraphQL type for the OurTeam model
class OurTeamType(DjangoObjectType):
    class Meta:
        model = OurTeam
        filter_fields = ['id']

# Define a query to list all team members
class Query(graphene.ObjectType):
    all_team_members = DjangoPaginationConnectionField(OurTeamType)

    def resolve_all_team_members(self, info, **kwargs):
        return OurTeam.objects.filter(**kwargs)


# Create the schema
schema = graphene.Schema(query=Query)
