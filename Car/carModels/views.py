from django.http import request
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import CarSerializer
from .models import Car
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import authentication,permissions
from rest_framework import status
from django.http import Http404
# Create your views here.

class CarListAPIView(APIView):
    def get(self, request, format ='json'):
        cars = Car.objects.all()
        serializer = CarSerializer(cars , many=True)
        return Response(serializer.data)


class CarCreateAPIView(APIView):
    def post(self, reuqest, format=None):
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)



class CarRetrieveAPIView(APIView):
    def get_object(self, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        pk = self.kwargs.get('pk')
        car = self.get_object(pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)


class CarUpdateAPIView(APIView):
      def get_object(self, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404


      def put(self,request,pk, format = None):
          pk=self.kwargs.get('pk')
          car = self.get_object('pk')
          serializer=CarSerializer(car , data = request.data)
          if Serializer.is_valid():
              serializer.save()
              return Response(serializer.data,status=status.HTTP_201_CREATED)
          return  Response(status=status.HTTP_400_BAD_REQUEST)
        
class CarDeleteAPIView(APIView):
      def get_object(self, *args, **kwargs):
        try:
            pk = self.kwargs.get('pk')
            return Car.objects.get(pk=pk)
        except Car.DoesNotExist:
            raise Http404
        
      def delete(self, request,pk):
          pk = self.kwargs.get('pk')
          car = self.get_object(pk)
          car.delete()
          return Response(status=status.HTTP_204_NO_CONTENT)

             

        

     

