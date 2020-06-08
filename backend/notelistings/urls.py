from django.urls import path 
from .views import ListingAllView, NoteView

urlpatterns = [
    path('list', ListingAllView.as_view()),
    path('<slug>', NoteView.as_view())
]
