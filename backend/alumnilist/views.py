from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Alumni
from rest_framework.response import Response

# Create your views here.


class AlumniCreateView(APIView):

  permission_classes = (permissions.AllowAny, )
  
  def post(self, request, format=None):
    data = self.request.data

    try :
      print(data)
      alumniDir = Alumni(name=data['name'], phone= data['phone'] , email= data['email'])
      alumniDir.save()
      return Response({'message': 'success'})
    except Exception as e:
      print(e)
      return Response({'message': 'failed but berhasil'})

  
