from django.shortcuts import render
from .serializers import ArticleSerializer
from rest_framework import viewsets      
from .models import Article                 

class ArticleView(viewsets.ModelViewSet):  
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer   
     