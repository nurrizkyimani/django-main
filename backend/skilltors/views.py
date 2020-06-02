from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Skilltor
from .serializers import SkilltorSerializer

class SkilltorListView(ListAPIView):
  permission_classes = (permissions.AllowAny, )
  queryset = Skilltor.objects.all()
  serializer_class = SkilltorSerializer
  pagination_class = None

class SkilltorView(RetrieveAPIView):
  queryset = Skilltor.objects.all()
  serializer_class = SkilltorSerializer

class TopSkilltorView(ListAPIView):
  permissions_classes = (permissions.AllowAny,)
  queryset = Skilltor.objects.filter(top_skilltor=True)
  serializer_class = SkilltorSerializer
  pagination_class = None
