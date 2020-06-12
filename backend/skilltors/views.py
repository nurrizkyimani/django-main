from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import Skilltor
from .serializers import SkilltorSerializer, SkilltorForm
from rest_framework.response import Response
from rest_framework.views import APIView


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


class AddSkilltorPost(APIView):
  permissions_classes = (permissions.AllowAny,)

  def post(self, request, format=None):
    data = self.request.data

    try: 
      skillowner = Skilltor(name=data['name'], phone=data['phone'],
        email=data['email'], top_skilltor=data['top_skilltor'])
      skillowner.save()
      return Response({'succes': 'Message send successfully'})
    except: 
      return Response({'error': 'Message failed to send'})