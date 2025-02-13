from django.urls import path
from .views import OurTeamListCreateView,OurTeamRetrieveUpdateDestroyView
from graphene_django.views import GraphQLView
from .schema import schema

urlpatterns = [
    path('team/',OurTeamListCreateView.as_view(),name='ourteam-list-create'),
    path('team/<int:pk>/',OurTeamRetrieveUpdateDestroyView.as_view(),name='ourteam-retrieve-update-destroy'),
    path('team/graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),
]