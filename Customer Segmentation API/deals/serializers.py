from django.db.models import fields
from rest_framework.serializers import ModelSerializer
from .models import Deals


class DealSerializer(ModelSerializer):
   class Meta:
        model = Deals
        fields = '__all__'