from rest_framework import generics
from .models import Company, CompanyTag, CompanyTeam, Users
from .serializers import CompanySmallSerializer, CompanySerializer, CompanyTagSerializer, CompanyTeamSerializer, UsersSerializer
from rest_framework.response import Response

from django.conf import settings
from rest_framework.exceptions import ValidationError


FRONTEND_URL = settings.FRONTEND_URL

# Create your views here.


class CompanyListCreateView(generics.ListCreateAPIView):
    queryset = Company.objects.all()
    serializer_class = CompanySmallSerializer
    # permission_classes = [permissions.IsAuthenticated]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return CompanySerializer
        return CompanySmallSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class CompanyRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CompanySerializer

    def get_queryset(self):
        user = self.request.user
        return Company.objects.filter(user=user)


class CompanyTagListCreateView(generics.ListCreateAPIView):
    queryset = CompanyTag.objects.all()
    serializer_class = CompanyTagSerializer


class CompanyTagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyTag.objects.all()
    serializer_class = CompanyTagSerializer


class CompanyTeamListCreateView(generics.ListCreateAPIView):
    queryset = CompanyTeam.objects.all()
    serializer_class = CompanyTeamSerializer


class CompanyTeamRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CompanyTeam.objects.all()
    serializer_class = CompanyTeamSerializer


class UsersListCreateView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def perform_create(self, serializer):
        email = self.request.data.get('email')
        if Users.objects.filter(email=email).exists():
            raise ValidationError(
                {'message': 'This email is already registered.'})

        user = serializer.save()
        user.is_activated = True
        user.save()


class UsersRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsersSerializer
    queryset = Users.objects.all()

    def get_object(self):
        # Get the user ID from the URL
        pk = self.kwargs.get('pk')
        return get_object_or_404(Users, id=pk)

    def get(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def patch(self, request, *args, **kwargs):
        user = self.get_object()
        serializer = self.get_serializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
