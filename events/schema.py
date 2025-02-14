import graphene
from graphene_django.types import DjangoObjectType
from .models import Event
from graphene_django_pagination import DjangoPaginationConnectionField


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        filter_fields = ['id','title']


class Query(graphene.ObjectType):
    all_events = DjangoPaginationConnectionField(EventType)

    def resolve_all_events(self, info, **kwargs):
        return Event.objects.all()


schema = graphene.Schema(query=Query)