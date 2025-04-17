from django.shortcuts import render
from serializers import Serializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Song, Artist
from .serializers import SongSerializer, ArtistSerializer, AlbumSerializer
from rest_framework.decorators import action
from rest_framework import permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework import generics
# Create your views here.


