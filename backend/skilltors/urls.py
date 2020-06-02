from django.urls import path
from .views import TopSkilltorView, SkilltorListView, SkilltorView


urlpatterns = [
  path('', SkilltorListView.as_view()),
  path('/topskilltor', TopSkilltorView.as_view()),
  path('/<pk>', SkilltorView.as_view()),
]