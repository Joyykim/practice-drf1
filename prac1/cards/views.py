from django.shortcuts import render

# Create your views here.
from rest_framework import views
from rest_framework.viewsets import ModelViewSet

from cards.models import Card
from cards.serializers import CardSerializer


class CardViewSet(ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
