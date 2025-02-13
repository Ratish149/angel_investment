import graphene
from graphene_django.types import DjangoObjectType
from .models import OurTeam

# Define a GraphQL type for the OurTeam model
class OurTeamType(DjangoObjectType):
    class Meta:
        model = OurTeam
        fields = "__all__"

# Define a query to list all team members
class Query(graphene.ObjectType):
    all_team_members = graphene.List(OurTeamType)
    team_member_by_id = graphene.Field(OurTeamType, id=graphene.Int(required=True))

    def resolve_all_team_members(self, info):
        return OurTeam.objects.all()

    def resolve_team_member_by_id(self, info, id):
        return OurTeam.objects.get(pk=id)

# Create the schema
schema = graphene.Schema(query=Query)
