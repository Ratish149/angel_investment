import graphene
from graphene_django.types import DjangoObjectType
from .models import Event, EventAttendee
from graphene_django_pagination import DjangoPaginationConnectionField


class EventType(DjangoObjectType):
    class Meta:
        model = Event
        filter_fields = ['id', 'title']


class EventAttendeeType(DjangoObjectType):
    class Meta:
        model = EventAttendee
        filter_fields = ['id', 'event', 'email', 'created_at']


class Query(graphene.ObjectType):
    all_events = DjangoPaginationConnectionField(EventType)

    def resolve_all_events(self, info, **kwargs):
        return Event.objects.all()


class CreateEventAttendee(graphene.Mutation):
    class Arguments:
        event_id = graphene.ID(required=True)
        email = graphene.String(required=True)

    event_attendee = graphene.Field(EventAttendeeType)

    def mutate(self, info, event_id, email):
        event = Event.objects.get(pk=event_id)
        attendee = EventAttendee.objects.create(event=event, email=email)
        return CreateEventAttendee(event_attendee=attendee)


class Mutation(graphene.ObjectType):
    create_event_attendee = CreateEventAttendee.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
