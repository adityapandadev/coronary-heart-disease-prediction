from rest_framework import serializers
from .models import CHD

class CHDSerializer(serializers.ModelSerializer):
    class Meta:
        model = CHD
        fields = "__all__"


