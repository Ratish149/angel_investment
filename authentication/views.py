from django.shortcuts import render, get_object_or_404, redirect
from rest_framework import generics
from .models import CustomUser, Company, CompanyTag, CompanyTeam, Users
from .serializers import CustomUserSerializer, LoginSerializer,CompanySmallSerializer, CompanySerializer, CompanyTagSerializer, CompanyTeamSerializer, UsersSerializer, VerifyLoginCodeSerializer
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
import time
import hashlib
import base64
import hmac
from rest_framework.decorators import api_view


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
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            html_message=html_message,
        )

def encode_user_id(user_id):
    """Encode user ID with timestamp to create activation token"""
    timestamp = str(int(time.time()))
    message = f"{user_id}:{timestamp}"
    # Create a hash using user_id, timestamp, and secret key
    signature = hashlib.sha256(f"{message}:{settings.SECRET_KEY}".encode()).hexdigest()[:8]
    # Combine all parts
    token = f"{message}:{signature}"
    # Convert to base64 to make it URL-safe
    return base64.urlsafe_b64encode(token.encode()).decode()

def decode_user_id(token, max_age=72*3600):  # 72 hours expiry
    try:
        # Decode base64
        decoded = base64.urlsafe_b64decode(token.encode()).decode()
        # Split parts
        user_id_str, timestamp_str, signature = decoded.rsplit(':', 2)
        # Verify signature
        message = f"{user_id_str}:{timestamp_str}"
        expected_signature = hashlib.sha256(f"{message}:{settings.SECRET_KEY}".encode()).hexdigest()[:8]
        if not hmac.compare_digest(signature, expected_signature):
            return None
        
        # Check timestamp
        timestamp = int(timestamp_str)
        if time.time() - timestamp > max_age:
            return None
        
        return int(user_id_str)
    except Exception:
        return None

@api_view(['POST'])
def activate_account(request):
    token = request.data.get('token')
    if not token:
        return Response({"error": "Activation token is required"}, status=status.HTTP_400_BAD_REQUEST)

    user_id = decode_user_id(token)
    if not user_id:
        return Response({"error": "Invalid or expired activation link"}, status=status.HTTP_400_BAD_REQUEST)

    user = get_object_or_404(Users, id=user_id)
    if not user.is_activated:
        user.is_activated = True
        user.save()

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)

        return Response({
            'message': "Account successfully activated",
            'user': UsersSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

    return Response({"message": "Account already activated"}, status=status.HTTP_200_OK)

# class LoginView(APIView):
#     serializer_class = LoginSerializer

#     def post(self, request):
        
#         email = request.data.get('email')
#         password = request.data.get('password')
#         user = authenticate(username=email, password=password)
         
#         if user is not None:
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 'message': "Login successful!",
#                 'user': CustomUserSerializer(user).data,
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#                 'is_active': user.is_activated
#             }, status=status.HTTP_200_OK)

#         else:
#             raise ValidationError({'error': 'Incorrect email or password.'})

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
            settings.DEFAULT_FROM_EMAIL,
            [new_email],
            html_message=html_message,
        )

def verify_email(request, user_id, new_email):
    user = get_object_or_404(Users, id=user_id)
    user.email = new_email
    user.username = new_email
    user.save()
    return redirect("https://investly-frontend-lyart.vercel.app/")

class UsersListCreateView(generics.ListCreateAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def perform_create(self, serializer):
        email = self.request.data.get('email')
        if Users.objects.filter(email=email).exists():
            raise ValidationError({'message': 'This email is already registered.'})

        user = serializer.save()
        user.is_activated = False
        user.save()
        
        # Send activation email with encoded token
        self.send_activation_email(user, email)

    def send_activation_email(self, user, email):
        # Generate activation token from user ID
        activation_token = encode_user_id(user.id)
        activation_link = f"http://localhost:3000/activate/{activation_token}/"
        
        subject = "Activate Your Angel Investment Account"
        html_message = render_to_string("activation_email.html", {
            "user": user, 
            "activation_link": activation_link
        })
        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            html_message=html_message,
        )

class UsersRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer


class UserLoginView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        email = request.data.get('email')
        if not email:
            raise ValidationError({'email': 'Email is required.'})
        
        user = Users.objects.filter(email=email).first()
        if not user:
            raise ValidationError({'email': 'User not found.'})
        if not user.is_activated:
            raise ValidationError({'email': 'User is not activated.'})

        # Generate verification code and save it to user model
        verification_code = self.generate_verification_code(user.id)
        user.verification_code = verification_code
        user.save()

        self.send_verification_code(user, verification_code)
        
        return Response({
            'message': 'Verification code sent to your email.',
            'email': email
        }, status=status.HTTP_200_OK)

    def generate_verification_code(self, user_id):
        timestamp = int(time.time() // 300)  # 300 seconds = 5 minutes
        message = f"{user_id}{timestamp}{settings.SECRET_KEY}"
        hash_object = hashlib.sha256(message.encode())
        return str(int(hash_object.hexdigest(), 16))[:6]

    def send_verification_code(self, user, code):
        subject = "Your Login Verification Code"
        html_message = render_to_string(
            "verification_code_email.html", 
            {
                "user": user, 
                "code": code
            }
        )
        plain_message = strip_tags(html_message)

        send_mail(
            subject,
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            html_message=html_message,
        )

class VerifyLoginCodeView(APIView):
    serializer_class = VerifyLoginCodeSerializer
    def post(self, request):
        email = request.data.get('email')
        submitted_code = request.data.get('code')

        if not all([email, submitted_code]):
            raise ValidationError({'error': 'Email and code are required'})

        user = Users.objects.filter(email=email).first()
        if not user:
            raise ValidationError({'error': 'User not found'})

        # Check the stored verification code
        if submitted_code != user.verification_code:
            raise ValidationError({'error': 'Invalid verification code'})

        # Clear the verification code after successful use
        user.verification_code = None
        user.save()

        # Create tokens and complete login
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'message': 'Login successful.',
            'user': UsersSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }, status=status.HTTP_200_OK)

    