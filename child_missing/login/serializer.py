from rest_framework  import serializers
from login.models import LoginTable
class android(serializers.ModelSerializer):
    class Meta:
        model=LoginTable
        fields= '__all__'