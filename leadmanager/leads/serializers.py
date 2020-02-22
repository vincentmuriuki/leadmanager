from rest_framework import serializers
from leads.models import Lead

# Lead Srializer
class LeadsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = '__all__'
         