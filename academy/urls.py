from django.urls import path
from .schema import schema
from graphene_django.views import GraphQLView

urlpatterns = [
    path('academy/graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]