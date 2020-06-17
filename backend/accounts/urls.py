from django.urls import path
from .views import SignupView, GoogleLogin

urlpatterns = [
    path('signup', SignupView.as_view()),
    # path('signin', SigninView.as_view())
    # path('auth/google', GoogleLogin.as_view(), name='google_login'),
]