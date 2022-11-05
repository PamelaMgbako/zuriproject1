 # serializers.py
from rest_framework import serializers

from musicapp.models import *

class ArtisteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = ('id', 'first_name', 'last_name', 'age')

class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = ('id' , 'title', 'artist_id', 'date_released')

class LyricsSerializer(serializers.ModelSerializer):
    class Meta:
            model = Lyrics
            fields = ('id', 'content', 'song_id')


