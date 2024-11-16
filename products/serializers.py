from rest_framework.serializers import ModelSerializer
from .models import Product
from users.serializers import UserSerializer
# from season.serializers.common import SeasonSerializer
# from badge.serializers.common import BadgeSerializer
# from category.serializers.common import CategorySerializer

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class PopulatedProductSerializer(ProductSerializer):
    owner = UserSerializer() # always execute the serializer with or without arguments
    # season = SeasonSerializer(many=True)
    # badge = BadgeSerializer(many=True)
    # category = CategorySerializer(many=True)