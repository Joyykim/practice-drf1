from django.shortcuts import render

# Create your views here.
from rest_framework import views
from rest_framework.viewsets import ModelViewSet

from cards.models import Card
from cards.serializers import CardSerializer


