from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from rest_framework import permissions
from .models import Skilltor
from .serializers import SkilltorSerializer, SkilltorForm
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.mixins import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics

from django.views.generic.edit import UpdateView
from django.http import Http404
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

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



class PostSkill(APIView):
    
    # def get(self, request):
    #     skilltors = Skilltor.objects.all()
    #     serializer = SkilltorSerializer(skilltors, many=True)
    #     return Response(serializer.data)

    
    def post(self, request):
        print('halo')
        print(request.data)
        # serializer = SkilltorForm(data=request.data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

