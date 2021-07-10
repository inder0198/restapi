from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework .views import APIView
from .serializers import student_serializer
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import student
from rest_framework.utils import json
# Create your views here.
class studentDetails(APIView):
    def post(self,request):
        student_data=student_serializer(data=request.data)
        if student_data.is_valid():
            student_data.save()
            return Response(({"status:":"success","reason":"DATA STORED"}),status=status.HTTP_201_CREATED)
        else:
            return Response(({"status:":"failed","reason":"DATA NOT STORED"}),status=status.HTTP_201_CREATED)

class ShowData(APIView):
    def post(self,request):
        data=list(student.objects.filter(address=request.data['address']).values('name','email','address','marks'))
        return HttpResponse(json.dumps({"status:":"success","response":data}),status=status.HTTP_201_CREATED)

class UpdateData(APIView):
    def post(self,request):
        student.objects.filter(address=request.data['address']).update(marks="500")
        data=list(student.objects.all().values('name','email','address','marks'))
        return HttpResponse(json.dumps({"status:":"success","response":data}),status=status.HTTP_201_CREATED)

class DisplayUsers(APIView):
    def get(self, request):
        data = list(student.objects.all().values('name','email','address','marks'))
        return HttpResponse(json.dumps({"status:":"success","response":data}),status=status.HTTP_201_CREATED)

class Task(APIView):
    def get(self, request,format=None):
        data = list(student.objects.all().values('name','email','address','marks'))
        return Response(data)
# to display data in response

class DeleteData(APIView):
    def post(self,request):
        student.objects.filter(name=request.data['name']).delete()
        data=list(student.objects.all().values('name','email','address','marks'))
        return HttpResponse(json.dumps({"status:":"success","response":data}),status=status.HTTP_201_CREATED)

class displaydata(viewsets.ModelViewSet):
    queryset=student.objects.all()
    serializer_class=student_serializer

    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

