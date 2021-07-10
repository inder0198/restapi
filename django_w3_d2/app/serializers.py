from rest_framework import serializers
from .models import *
class student_serializer(serializers.ModelSerializer):
    class Meta():
        model=student
        fields="__all__"