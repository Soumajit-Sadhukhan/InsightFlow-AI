from django.shortcuts import render
from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Project
from .serializers import ProjectSerializer

# Create your views here.

class ProjectCreateView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    
    def post(self, request):
        
        serializer = ProjectSerializer(data=request.data)
        
        if serializer.is_valid():
            
            serializer.save(owner=request.user)
            
            return Response(
                {
                    "status": "success",
                    "message": "Project created successfully",
                    "data": serializer.data,
                },
                status=status.HTTP_201_CREATED,
            )
        return Response(
            {
                "status": "error",
                "errors": serializer.errors,
                    
            },
            status=status.HTTP_400_BAD_REQUEST
        )

class ProjectListView(APIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    
    def get(self, request):
        
        projects = Project.objects.filter(owner=request.user)
        
        serializer = ProjectSerializer( projects, many=True)
        
        return Response(
            {
                "status": "success",
                "count": projects.count(),
                "data": serializer.data,
            },
            status=status.HTTP_200_OK
        )

class ProjectDetailView(APIView):
    
    permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer
    
    def get(self, request, pk):
        project = get_object_or_404(
            Project,
            pk=pk,
            owner=request.user
            
        )
        serializer = ProjectSerializer(project)
        
        return Response(
            {
                "status": "success",
                "data": serializer.data,
            },
            status=status.HTTP_200_OK
        )
        
    def put(self, request, pk):
        project = get_object_or_404(
            Project,
            pk=pk,
            owner=request.user
        )
        
        serializer = ProjectSerializer(project, data=request.data)
        
        if serializer.is_valid():
            
            serializer.save()
            
            return Response(
                {
                    "status":"success",
                    "message": "Project updated successfully",
                    "data": serializer.data,
                    
                },
                status=status.HTTP_200_OK
            )
        return Response(
            {
                "status": "error",
                "errors": serializer.errors
            },
            status=status.HTTP_400_BAD_REQUEST
        )
        
    def delete(self, request, pk):
        
        project = get_object_or_404(
            Project,
            pk=pk,
            owner = request.user
        ) 
        
        project.delete()
        
        return Response(
            {
                "status":"success",
                "message":"Project deleted successfully",
            },
            status=status.HTTP_200_OK
        )