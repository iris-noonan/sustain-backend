from rest_framework.serializers import ModelSerializer
from .models import Product
from users.serializers import UserSerializer
from seasonality.serializers.common import SeasonSerializer
from badges.serializers.common import BadgeSerializer
from categories.serializers.common import CategorySerializer

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PopulatedProductSerializer(ProductSerializer):
    owner = UserSerializer() # always execute the serializer with or without arguments
    seasonality = SeasonSerializer(many=True)
    badges = BadgeSerializer(many=True)
    categories = CategorySerializer(many=True)