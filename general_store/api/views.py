from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

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