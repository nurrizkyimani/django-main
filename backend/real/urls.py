from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView



urlpatterns = [
    path('accounts/', include('allauth.urls')),
    path('api-auth/', include('rest_framework.urls')),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/accounts/', include('accounts.urls')),
    path('api/profils/', include('profils.urls')),
    path('api/notelistings/', include('notelistings.urls')),
    path('admin/', admin.site.urls),

    path('', include('social_django.urls', namespace='social')),
    # path('logout/', logout, {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),

    re_path('o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    # re_path(r'^oauth/', include('social_django.urls', namespace='social')),
    # path('', include('social.apps.django_app.urls', namespace='social')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
