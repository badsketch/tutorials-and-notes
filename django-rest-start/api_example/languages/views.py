from django.shortcuts import render
from rest_framework import viewsets
from .models import Language
from .serializers import LanguageSerializer

# to specify what happens for each CRUD operation
# this is also a default
class LanguageView(viewsets.ModelViewSet):
    queryset = Language.objects.all()
    serializer_class = LanguageSerializer