from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import ProfilSerializer
from .models import Profils


class AddNewProfilPost(APIView):
  permission_classes = (permissions.AllowAny, )
  
  def post(self, request, format=None):
    data = self.request.data
    try :
      print(data)
      profils = Profils(
        avatar = data['avatar'],
        description = data['description'],
        chat = data['chat'],
        linkedin = data['linkedin'],
        about = data['about'],
        experience = data['experience'],
        major = data['major'],
        skill = data['skill'],
        topics = data['topics']
      )

      profils.save()
      return Response({'message': 'success'})
    except Exception as e:
      print(e)
      return Response({'message': 'failed but berhasil from skilltor'})


class ProfilListView(ListAPIView):
  permission_classes = (permissions.AllowAny, )
  queryset = Profils.objects.all()
  serializer_class = ProfilSerializer
  pagination_class = None

class ProfilView(RetrieveAPIView):
  queryset = Profils.objects.all()
  serializer_class = ProfilSerializer


  