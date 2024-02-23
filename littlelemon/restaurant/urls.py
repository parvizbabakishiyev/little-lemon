#define URL route for index() view
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from . import views


urlpatterns = [
  path('index/', views.index, name='index'),
  path('items/', views.MenuItemsView.as_view(), name='menu-items'),
  path('items/<int:pk>', views.SingleMenuItemView.as_view(), name='menu-item'),
  path('api-token-auth/', obtain_auth_token),
]
