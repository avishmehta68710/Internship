from django.shortcuts import render,HttpResponse,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import blogs
from .serializor import blogserilizer

# Create your views here.

class bloglist(APIView):
    def get(self,request):
        lists = blogs.objects.all()
        serializer = blogserilizer(lists,many=True)
        return Response(serializer.data)

