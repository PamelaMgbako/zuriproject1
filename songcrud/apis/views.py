import dataclasses
from django.shortcuts import render
from musicapp.models import *
from django.http import Http404
from rest_framework import permissions
from rest_framework import generics
from rest_framework import status
from rest_framework import serializers
from rest_framework.response import Response
from .serializers import ArtisteSerializer, SongSerializer, LyricsSerializer

# Create your views here.
class ArtisteAPIView(generics.ListAPIView):

    
    queryset = Artiste.objects.all()
    serializer_class = ArtisteSerializer
    permission_classes = [permissions.IsAuthenticated]


class SongAPIView(generics.ListAPIView):

    
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = [permissions.IsAuthenticated]

class SongDetailsAPIView(generics.ListAPIView):

    
    serializer_class = SongSerializer
def get_object(self, pk):
        try:
            return Song.objects.get(pk=pk)
        except Song.DoesNotExist:
         return Http404

def get(self, request,pk,format=None):
        song = self.get_object(pk)
        return Response(serializers.data)

def delete(self,request,pk,format=None):
       song = self.get_object(pk)
       song.delete()
       return Response(status=status.HTTP_404_NOT_FOUND)

def delete(self,request,pk,format=None):
       song = self.get_object(pk)
       serializer = SongSerializer(song, data=request.data)
       if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
       return Response(serializer.errors, status=status.HTTP_404_BAD_REQUEST)

class LyricsAPIView(generics.ListAPIView):

    
    queryset = Lyrics.objects.all()
    serializer_class = LyricsSerializer
    permission_classes = [permissions.IsAuthenticated]


