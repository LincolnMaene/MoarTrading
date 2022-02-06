import imp
from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.http import JsonResponse
from rest_framework.views import APIView
from rest_framework.response import Response

class home_view(View):
    def get(self,request, *args, **kwargs):
        return render(request, 'home.html', {})

class data_test_view (APIView):

    authentication_classes=[]
    permission_classes=[]

    def get(self,request, format=None):
        data={

            "sales":100,
            "customers":10,
        }
        return Response(data)

def data_test_view_2(request, *args, **kwargs):
        data={

            "sales":100,
            "customers":10,
        }
        return JsonResponse(data)