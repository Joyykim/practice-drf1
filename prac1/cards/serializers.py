from rest_framework.fields import ReadOnlyField
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import ModelSerializer

from cards.models import Card


class CardSerializer(ModelSerializer):
    owner = ReadOnlyField(source='owner.username')
    # owner = UserSerializer()

    class Meta:
        model = Card
        fields = ('id', 'content', 'owner')
