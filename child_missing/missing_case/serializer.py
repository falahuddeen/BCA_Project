from rest_framework  import serializers
from missing_case.models import MissingCaseTable
class android(serializers.ModelSerializer):
    class Meta:
        model=MissingCaseTable
        fields= '__all__'