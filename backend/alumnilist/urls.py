from django.urls import path
from .views import AlumniCreateView

urlpatterns = [
    path('', AlumniCreateView.as_view()),
]