from rest_framework  import serializers
from emergency_number.models import EmergencyNumberTable
class android(serializers.ModelSerializer):
    class Meta:
        model=EmergencyNumberTable
        fields= '__all__'