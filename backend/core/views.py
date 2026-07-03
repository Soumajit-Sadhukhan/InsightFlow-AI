from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class HealthCheckView(APIView):
    def get(self, rewuest):
        return Response({
            "status": "success",
            "massage": "InsightFlow AI Backend is Running 🚀"
        })