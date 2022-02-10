from http import server
from os import stat
from shutil import move

from django.http import HttpResponse
from watchlist_app.models import WatchList, StreamPlatForm
from watchlist_app.api.serializers import WatchListSerializers, StreamPlatformSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.decorators import APIView

class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializers = WatchListSerializers(movies, many=True)
        return Response(serializers.data)
    
    def post(self, request):
        movie = WatchList.objects.all()
        serializers = WatchListSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors)

class WatchDetailAV(APIView):
    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response({"Error" : "Movie not Found"}, status=status.HTTP_404_NOT_FOUND)

        serializers = WatchListSerializers(movie)
        return Response(serializers.data)
    
    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        serializers = WatchListSerializers(movie, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors())

    def delete(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class StreamPlatformListAV(APIView):

    def get(self, request):
        platforms = StreamPlatForm.objects.all()
        serializers = StreamPlatformSerializers(platforms, many=True)
        return Response(serializers.data)
    
    def post(self, request):
        platforms = StreamPlatForm.objects.all()
        serializers = StreamPlatformSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)

class StreamPlatformDetailAV(APIView):

    def get(self, request, pk):
        try:
            platform = StreamPlatForm.objects.get(pk=pk)
        except StreamPlatForm.DoesNotExist:
            return Response({"Error" : "Platform not found"}, status=status.HTTP_204_NO_CONTENT)
    
        serializers = StreamPlatformSerializers(platform)
        return Response(serializers.data)
    
    def put(self, request, pk):
        platform = StreamPlatForm.objects.get(pk=pk)
        serializers = StreamPlatformSerializers(platform, data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
    
    def delete(self, request, pk):
        platform = StreamPlatForm.objects.get(pk=pk)
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


#Function based views

# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET':
#         movies = Movie.objects.all()
#         serializers = MovieSerializers(movies, many=True)
#         return Response(serializers.data)
    
#     if request.method == 'POST':
#         serializers = MovieSerializers(data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)

#         else:
#             return Response(serializers.errors)

# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request, pk):
#     if request.method == 'GET':
#         try:

#             movie = Movie.objects.get(pk=pk)
#         except Movie.DoesNotExist:
#             return Response({"Error": "Movie not found"}, status=status.HTTP_404_NOT_FOUND)
#         serializers = MovieSerializers(movie)
#         return Response(serializers.data)
    
#     if request.method == 'PUT':
#         movie = Movie.objects.get(pk=pk)
#         serializers = MovieSerializers(movie, data=request.data)
#         if serializers.is_valid():
#             serializers.save()
#             return Response(serializers.data)
#         else:
#             return Response(serializers.errors(), status=status.HTTP_400_BAD_REQUEST)

#     if request.method == 'DELETE':
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

        

