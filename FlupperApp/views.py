from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import Http404
from rest_framework import status
import io
from rest_framework.parsers import JSONParser


class FlupperFashionShow(APIView):

    def get(self, request, format=None):
        events = Category.objects.all()
        serializer = CategorySerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #json_data=request.body
        #stream=io.BytesIO(json_data)
        #data=JSONParser().parse(stream)
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    """
    Retrieve, update or delete a snippet instance.
    """

    def get_object(self, pk):
        try:
            return Category.objects.get(pk=pk)
        except Category.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        events = self.get_object(pk=pk)
        serializer = CategorySerializer(events)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        events = self.get_object(pk=pk)
        serializer = CategorySerializer(events, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        events = self.get_object(pk)
        events.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class FlupperFashionShow1(APIView):
    def get(self, request, format=None):
        events = Category_details.objects.all()
        serializer = Category_detailSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        #json_data = request.body
        #stream = io.BytesIO(json_data)
        #data = JSONParser().parse(stream)

        serializer = Category_detailSerializer(data=request.data)

        file = request.data
        #event_image = Category_details.objects.create(event_image=file)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Category_Detail(APIView):
    def get_object(self, pk):
        try:
            return Category_details.objects.get(pk=pk)
        except Category_details.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        events = self.get_object(pk=pk)
        serializer = Category_detailSerializer(events)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        events = self.get_object(pk)
        serializer = Category_detailSerializer(events, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        events = self.get_object(pk)
        events.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

