from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .models import CustomUser, Company, CompanyTag, CompanyTeam
from .serializers import CustomUserSerializer, LoginSerializer,CompanySmallSerializer, CompanySerializer, CompanyTagSerializer, CompanyTeamSerializer
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings
from django.http import HttpResponse
from rest_framework.exceptions import ValidationError
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.views import APIView
from django.contrib.auth import authenticate


# Create your views here.

class CustomUserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class CustomUserRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise ValidationError({'email': 'This email is already in use.'})

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        user.is_activated = False  # Keep inactive until verified
        user.save()

        # Send activation email
        self.send_activation_email(user)

        refresh = RefreshToken.for_user(user)
        return Response({
            'message': "Registration successful! Please check your email to activate your account.",
            'user': CustomUserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_201_CREATED)

    def send_activation_email(self, user):
        activation_link = f"http://investly.baliyoventures.com/api/activate/{user.id}/"

        subject = "Activate Your Angel Investment Account"
        html_message = render_to_string("activation_email.html", {"user": user, "activation_link": activation_link})
        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            settings.EMAIL_HOST_USER,
            [user.email],
            html_message=html_message,
        )

def activate_account(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)

    if not user.is_active:
        user.is_activated = True
        user.save()
        return redirect("https://investly-frontend-lyart.vercel.app/")

    return HttpResponse("Account already activated.")

class LoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        
        email = request.data.get('email')
        password = request.data.get('password')
        user = authenticate(username=email, password=password)
         
        if user is not None:
            refresh = RefreshToken.for_user(user)
            return Response({
                'message': "Login successful!",
                'user': CustomUserSerializer(user).data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                'is_active': user.is_activated
            }, status=status.HTTP_200_OK)

        else:
            raise ValidationError({'error': 'Incorrect email or password.'})

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

class ChangeEmailView(generics.UpdateAPIView):
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def update(self, request, *args, **kwargs):
        user = self.request.user
        new_email = request.data.get('new_email')

        if CustomUser.objects.filter(email=new_email).exists():
            raise ValidationError({'new_email': 'This email is already in use.'})

        self.send_verification_email(user, new_email)  # Pass user.id and new_email to the method

        return Response({'message': 'A verification email has been sent to your new email address. Please click the link in the email to verify your new email.'}, status=status.HTTP_200_OK)

    def send_verification_email(self, user, new_email):
        verification_link = f"https://investly.baliyoventures.com/api/verify/{user.id}/email/{new_email}/"

        subject = "Verify Your New Email"
        html_message = render_to_string("verify_email.html", {"user": user, "verification_link": verification_link, "new_email": new_email})
        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            settings.EMAIL_HOST_USER,
            [new_email],
            html_message=html_message,
        )
def verify_email(request, user_id, new_email):
    user = get_object_or_404(CustomUser, id=user_id)
    user.email = new_email
    user.username = new_email
    user.save()
    return redirect("https://investly-frontend-lyart.vercel.app/")

    
