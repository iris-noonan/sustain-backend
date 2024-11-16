from rest_framework.serializers import ModelSerializer
from ..models import Badge

class BadgeSerializer(ModelSerializer):
    class Meta:
        model = Badge
        fields = '__all__'
