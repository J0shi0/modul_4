from .models import Task, Comment, Tag
from .serializers import TaskSerializer, CommentSerializer, TagSerializer
from .permissions import IsOwner

from django.shortcuts import render

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, generics, mixins


def base(requests):
    return render(requests, template_name='base.html')


def about_us(requests):
    return render(requests, template_name='about_us.html')


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (IsAuthenticated, IsOwner)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAuthenticated,)


class CommentListCreateAPIVIew(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)


class CommentRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)
