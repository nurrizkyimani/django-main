from django.urls import path
from .views import AddNewProfilPost, ProfilListView, ProfilView

urlpatterns = [
  path('post', AddNewProfilPost.as_view()),
  path('<pk>',ProfilView.as_view() ),
  path('list', ProfilListView.as_view())
]