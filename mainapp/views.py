from django.shortcuts import get_object_or_404, render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import *
from .serializers import *

class TeacherAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        teachers = Teacher.objects.all()
        serializer = TeacherSeralizer(teachers, many=True)
        return Response({'teachers': serializer.data})
    
    def post(self,request):
        serializer = TeacherSeralizer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'teachers': serializer.data})
        return Response(serializer.errors)
            
        
class TeacherDetailAPIView(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request, pk):
        teachers = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSeralizer(teachers)
        return Response({'teachers': serializer.data})

    def put(self, request, pk):
        teachers = get_object_or_404(Teacher, pk=pk)
        serializer = TeacherSeralizer(teachers, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'teachers': serializer.data})
        return Response(serializer.errors)

    def delete(self, request, pk):
        teachers = get_object_or_404(Teacher, pk=pk)
        teachers.delete()
        return Response()