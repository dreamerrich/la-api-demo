from django.shortcuts import render
from .models import Project
from .serializers import projectSerializers
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from rest_framework import filters
# Create your views here.

#------------- creating data --------------
class projectList(APIView):
    permission_classes = [IsAuthenticated, ]
    filter_backends = (filters.SearchFilter,)
    search_fields = ['project_name', 'color']

    def filter_queryset(self, queryset):
        for backend in list(self.filter_backends):
            queryset = backend().filter_queryset(self.request, queryset, self)
            print("🚀 ~ file: views.py ~ line 21 ~ queryset", queryset)
        return queryset

    def get_queryset(self):
        return Project.objects.all().order_by("created_at")
        # return Project.objects.all().order_by("-created_at")

    def get(self, request, format=None):
        the_filtered_qs = self.filter_queryset(self.get_queryset())
        serializer = projectSerializers(the_filtered_qs, many=True)
        print("🚀 ~ file: views.py ~ line 30 ~ serializer", serializer)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = projectSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#------------- CRUD operations ------------
class projectDetails(APIView):
    def get_object(self, pk):

        print("🚀 ~ file: views.py ~ line 44 ~ id", pk)
        try:
            return Project.objects.get(pk=pk)
        except Project.DoesNotExist as e:
            raise Http404 from e

    def get(self, request, pk, format=None):
        project_data = self.get_object(pk)
        serializer = projectSerializers(project_data)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        project_data = self.get_object(pk)
        serializer = projectSerializers(project_data, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project_data = self.get_object(pk)
        project_data.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

