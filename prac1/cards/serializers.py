from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from cards.models import Card


class CardSerializer(ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Card
        fields = ('id', 'content', 'owner')
