from rest_framework import serializers
from .models import Profils


class ProfilSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profils
    fields = '__all__'

class SkilltorForm(serializers.ModelSerializer):
  class Meta:
    model = Profils
    fields = ('name')
    

  