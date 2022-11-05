from django.urls import include, path
from rest_framework import routers
from .import views

urlpatterns = [
path('artiste/', views.ArtisteAPIView.as_view()),
path('song/', views.ArtisteAPIView.as_view()),
path('song/<int:pk>', views.SongDetailsAPIView.as_view()),
path('lyrics/', views.ArtisteAPIView.as_view()),

]