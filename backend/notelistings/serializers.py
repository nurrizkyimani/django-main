from rest_framework import serializers
from .models import Note

class NoteListingsSerializer(serializers.ModelSerializer):
  class Meta: 
    model : Note
    fields: ('title', 'instructor', 'semester', 'year', 'course', 'description', 'photo_main', 'upload_date', 'sale_type')

class NoteDetailSerializer(serializers.ModelSerializer):
  class Meta:
    model: Note
    fields: '__all__'
    lookup_field: 'slug'
