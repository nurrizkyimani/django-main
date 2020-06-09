from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Skilltor
from .serializers import SkilltorSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
# from rest_framework.mixins import mixins
from rest_framework.permissions import IsAuthenticated

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


class postSkilltorView(APIView):
  permission_classes = [IsAuthenticated]
  def post(self, request):
    data = self.request.data
    serializer = SkilltorSerializer(data=data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response({"message": "Data accepted", "data": request.data})
