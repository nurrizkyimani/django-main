from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from rest_framework.response import Response
from .models import Note
from .serializers import NoteListingsSerializer, NoteDetailSerializer
from rest_framework.views import APIView
from datetime import datetime, timezone, timedelta


class ListingAllView(ListAPIView):
  queryset = Note.objects.order_by('-upload_date').filter(is_published=True)
  permission_classes = (permissions.AllowAny,)
  serializer_class = NoteListingsSerializer
  lookup_field = 'slug'

class NoteView(RetrieveAPIView):
  queryset = Note.objects.order_by('-upload_date').filter(is_published=True)
  permission_classes =  (permissions.AllowAny,)
  serializer_class = NoteDetailSerializer
  lookup_field = 'slug'

