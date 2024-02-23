from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers

# Create your views here.
class MenuItemsView(ListCreateAPIView):
  queryset = models.Menu.objects.all()
  serializer_class = serializers.MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
  queryset = models.Menu.objects.all()
  serializer_class = serializers.MenuSerializer

class BookingViewSet(ModelViewSet):
  permission_classes = [IsAuthenticated]
  queryset = models.Booking.objects.all()
  serializer_class = serializers.BookingSerializer