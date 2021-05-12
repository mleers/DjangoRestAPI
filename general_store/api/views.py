from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ItemSerializer

from .models import Item
# Create your views here.

@api_view(['GET'])
def apiOverview(request):
    api_urls = {
	    'List':'/item-list/',
	    'Detail View':'/item-detail/<str:pk>/',
	    'Create':'/item-create/',
	    'Update':'/item-update/<str:pk>/',
	    'Delete':'/item-delete/<str:pk>/',
	    }
    return Response(api_urls)

@api_view(['GET'])
def itemList(request):
	items = Item.objects.all()
	serializer = ItemSerializer(items, many=True)
	return Response(serializer.data) # query db, serialize data,return it in response