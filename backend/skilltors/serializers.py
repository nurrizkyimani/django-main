from rest_framework import serializers
from .models import Skilltor


class SkilltorSerializer(serializers.ModelSerializer):
  class meta:
    model = Skilltor
    fields = '__all__'
    

  
