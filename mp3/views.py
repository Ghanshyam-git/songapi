from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from mp3.serializer import *
from mp3.models import *

# Create your views here.
class getSongList(APIView):
    @staticmethod
    def post(request):
            userobj = Song.objects.all()
            serobj = songserializer(userobj, many=True)
            return Response({'message':'song List','res':serobj.data},status=200)
        
class Create_Song(APIView):
    @staticmethod
    def post(request):
        try:
            schoolser = songserializer(data = request.data)
            if schoolser.is_valid():
                schoolser.save()
                return Response({'message':" song Registration SuccesFull",'res':schoolser.data,},status=200)
            else:
                return Response(schoolser.errors, status=status.HTTP_400_BAD_REQUEST)
        except (ObjectDoesNotExist, KeyError):
            return Response({'message':"Invalid User id"}, status=404)
        
        
class Update_Song(APIView):
    @staticmethod
    def post(request):
        try:
            products = Song.objects.get(id=request.data['s_id'])
            serobj = songserializer(products,data = request.data, partial = True)
            if serobj.is_valid():
                serobj.save()
                return Response({"message":"song update successfully",'res':serobj.data,},status=200)
            else:
                return Response(serobj.errors, status=status.HTTP_400_BAD_REQUEST)
        except(ObjectDoesNotExist, KeyError):
            return Response({'message':"Invalid song Id"}, status=404)
        
        
class deleteSong(APIView):
    @staticmethod
    def post(request):
        try:
            products = Song.objects.get(id=request.data['s_id'])
            products.delete()
            return Response({"message":"song delete successfully"},status=200)
        except(ObjectDoesNotExist, KeyError):
            return Response({'message':"Invalid song Id"}, status=404)
