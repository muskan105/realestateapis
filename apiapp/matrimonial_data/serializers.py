from rest_framework import serializers
from .models import Ghar

class GharSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ghar
        fields = '__all__'