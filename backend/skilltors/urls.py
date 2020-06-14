from django.urls import path
from .views import TopSkilltorView, SkilltorListView, SkilltorView
from .views import  AddSkilltorPost


urlpatterns = [
  path('post', AddSkilltorPost.as_view()),
  path('skill', SkilltorListView.as_view()),
  path('top', TopSkilltorView.as_view()),
  path('<pk>', SkilltorView.as_view()),
]