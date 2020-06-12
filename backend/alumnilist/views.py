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
    print(data)
   
    contact = Alumni(name=data['name'], email=data['email'], phone=data['phone'])
    contact.save()
      # alumniDir = Alumni(name=data['name'], phone= data['phone'] , email= data['email'])
      # alumniDir.save()
    # return Response({'message': 'success'})

    return Response({'message': 'failed but berhasil'})