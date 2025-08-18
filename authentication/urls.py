from django.urls import path
from .views import CompanyListCreateView, CompanyRetrieveUpdateDestroyView, CompanyTagListCreateView, CompanyTagRetrieveUpdateDestroyView, CompanyTeamListCreateView, CompanyTeamRetrieveUpdateDestroyView, UsersListCreateView, UsersRetrieveUpdateDestroyView
from graphene_django.views import GraphQLView
from .schema import schema


urlpatterns = [

    path('companies/', CompanyListCreateView.as_view(),
         name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(),
         name='company-retrieve-update-destroy'),
    path('tags/', CompanyTagListCreateView.as_view(),
         name='company-tag-list-create'),
    path('tags/<int:pk>/', CompanyTagRetrieveUpdateDestroyView.as_view(),
         name='company-tag-retrieve-update-destroy'),
    path('teams/', CompanyTeamListCreateView.as_view(),
         name='company-team-list-create'),
    path('teams/<int:pk>/', CompanyTeamRetrieveUpdateDestroyView.as_view(),
         name='company-team-retrieve-update-destroy'),

    # Enable GraphiQL interface
    path('auth/graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),

    path('users/', UsersListCreateView.as_view(), name='users-list-create'),
    path('users/<int:pk>/', UsersRetrieveUpdateDestroyView.as_view(),
         name='user-profile'),

]
