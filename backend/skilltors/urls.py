from django.urls import path
from .views import TopSkilltorView, SkilltorListView, SkilltorView, PostSkill


urlpatterns = [
  path('', SkilltorListView.as_view()),
  path('top', TopSkilltorView.as_view()),
  path('<pk>', SkilltorView.as_view()),
  # path('snippets/', views.SnippetList.as_view()),
  path('post', PostSkill.as_view()),
]