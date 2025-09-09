from rest_framework import serializers
from .models import FoundID, LostIDReport

class FoundIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoundID
        fields = '__all__'

class LostIDReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = LostIDReport
        fields = '__all__'
