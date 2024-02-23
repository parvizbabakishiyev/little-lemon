from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, DestroyAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers

# Create your views here.
def index(request):
  return render(request, 'index.html', {})

class MenuItemsView(ListCreateAPIView):
  permission_classes = [IsAuthenticated]
  queryset = models.Menu.objects.all()
  serializer_class = serializers.MenuSerializer


class SingleMenuItemView(RetrieveUpdateAPIView, DestroyAPIView):
  permission_classes = [IsAuthenticated]
  queryset = models.Menu.objects.all()
  serializer_class = serializers.MenuSerializer

class BookingViewSet(ModelViewSet):
  permission_classes = [IsAuthenticated]
  queryset = models.Booking.objects.all()
  serializer_class = serializers.BookingSerializer