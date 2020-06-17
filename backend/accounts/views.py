from django.contrib.auth import get_user_model
User = get_user_model()

from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from django.shortcuts import render

# Create your views here.



class SignupView(APIView):
    permission_classes = (permissions.AllowAny, )

    def post(self, request, format=None):
        data = self.request.data

        name = data['name']
        email = data['email']
        username = data['username']
        password = data['password']
        password2 = data['password2']
        

        if password == password2:
            if User.objects.filter(email=email).exists():
                return Response({'error': 'Email already exist'})
            else:
                if len(password) < 6:
                    return Response({'error': 'Password must be at least 6 characters'})
                else:
                    user = User.objects.create_user(
                        email=email, password=password, name=name, username=username)

                    user.save()
                    return Response({'success': 'User crearted successfully'})
        else:
            return Response({'error': 'Password do not match'})

from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from rest_auth.registration.views import SocialLoginView


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client