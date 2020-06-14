from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from .models import Skilltor
from .serializers import SkilltorSerializer, SkilltorForm
from rest_framework.response import Response
from rest_framework.views import APIView


class AddSkilltorPost(APIView):
  permission_classes = (permissions.AllowAny, )
  
  def post(self, request, format=None):
    data = self.request.data
    try :
      print(data)
      skillowner = Skilltor(name=data['name'], phone=data['phone'], email=data['email'], top_skilltor=data['top_skilltor'], description=data['description'])
      skillowner.save()
      return Response({'message': 'success'})
    except Exception as e:
      print(e)
      return Response({'message': 'failed but berhasil from skilltor'})


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


  