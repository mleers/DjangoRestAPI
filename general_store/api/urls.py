from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('item-list/', views.itemList, name="item-list"),
    path('item-detail/<str:pk>', views.itemDetail, name="item-detail"),
    path('item-create/', views.itemCreate, name="item-create"),

]