from rest_framework import viewsets, generics, mixins

from django.shortcuts import render
from .models import Task, Comment, Tag
from .serializers import TaskSerializer, CommentSerializer, TagSerializer


def base(requests):
    return render(requests, template_name='base.html')


def about_us(requests):
    return render(requests, template_name='about_us.html')


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class CommentListCreateAPIVIew(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
