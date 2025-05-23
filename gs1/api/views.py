from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from django.http import HttpResponse, JsonResponse


# Create your views here.

def student_details(request,pk):
    stu= Student.objects.get(id=pk)
    serializer = StudentSerializer(stu)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data,content_type='application/json')


def all_student_details(request):
    stu=Student.objects.all()
    serializer= StudentSerializer(stu, many= True)
    # json_data= JSONRenderer().render(serializer.data)
    # return HttpResponse(json_data,content_type= 'application/json')
    return JsonResponse(serializer.data, safe=False)
