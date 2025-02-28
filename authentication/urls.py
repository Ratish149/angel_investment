from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView
from .views import UserRegistrationView, UserLoginView,CustomUserListCreateView, CustomUserRetrieveUpdateDestroyView, CompanyListCreateView, CompanyRetrieveUpdateDestroyView, CompanyTagListCreateView, CompanyTagRetrieveUpdateDestroyView, CompanyTeamListCreateView, CompanyTeamRetrieveUpdateDestroyView, VerifyLoginCodeView,activate_account, ChangeEmailView,verify_email, UsersListCreateView, UsersRetrieveUpdateDestroyView
from graphene_django.views import GraphQLView
from .schema import schema


urlpatterns = [
    # path('users/', CustomUserListCreateView.as_view(), name='user-list'),
    # path('users/<int:pk>/', CustomUserRetrieveUpdateDestroyView.as_view(), name='user-detail'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('change-email/', ChangeEmailView.as_view(), name='change-email'),
    path('verify/<int:user_id>/email/<str:new_email>/', verify_email, name='verify-email'),

    path('companies/', CompanyListCreateView.as_view(), name='company-list-create'),
    path('companies/<int:pk>/', CompanyRetrieveUpdateDestroyView.as_view(), name='company-retrieve-update-destroy'),
    path('tags/', CompanyTagListCreateView.as_view(), name='company-tag-list-create'),
    path('tags/<int:pk>/', CompanyTagRetrieveUpdateDestroyView.as_view(), name='company-tag-retrieve-update-destroy'),
    path('teams/', CompanyTeamListCreateView.as_view(), name='company-team-list-create'),
    path('teams/<int:pk>/', CompanyTeamRetrieveUpdateDestroyView.as_view(), name='company-team-retrieve-update-destroy'),

    path('activate/', activate_account, name='activate-account'),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('auth/graphql/', GraphQLView.as_view(graphiql=True, schema=schema)),  # Enable GraphiQL interface

    path('users/', UsersListCreateView.as_view(), name='users-list-create'),
    path('users/profile/', UsersRetrieveUpdateDestroyView.as_view(), name='user-profile'),
    path('verify-login-code/', VerifyLoginCodeView.as_view(), name='verify-login-code'),

]
