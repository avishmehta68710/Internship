from django.http import HttpResponse
from .models import blogs
from rest_framework import response
from rest_framework import serializers

class blogserilizer(serializers.ModelSerializer):

    class Meta:
        model = blogs
        fields = "__all__"
