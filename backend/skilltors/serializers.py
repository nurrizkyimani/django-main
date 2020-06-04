from rest_framework import serializers
from .models import Skilltor


class SkilltorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Skilltor
    fields = '__all__'
    

  
