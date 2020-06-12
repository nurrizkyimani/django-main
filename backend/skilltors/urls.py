from django.urls import path
from .views import TopSkilltorView, SkilltorListView, SkilltorView, AddSkilltorPost


urlpatterns = [
  path('', SkilltorListView.as_view()),
  path('top', TopSkilltorView.as_view()),
  path('<pk>', SkilltorView.as_view()),
  path('post', AddSkilltorPost.as_view()),
]