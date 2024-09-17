from .models import Task, Comment, Tag
from .serializers import TaskSerializer, CommentSerializer, TagSerializer
from .permissions import IsOwner
from .tasks import check_and_replace_prohibited_words

from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, generics, mixins


def base(requests):
    return render(requests, template_name='base.html')


def about_us(requests):
    return render(requests, template_name='about_us.html')


@method_decorator(cache_page(60 * 15), name='get')
class TagListView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = (AllowAny, IsOwner)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (AllowAny,)


class CommentCreateView(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        comment = serializer.save()
        check_and_replace_prohibited_words.delay(comment.id)


class CommentListView(generics.ListAPIView):
    permission_classes = (AllowAny,)
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentRetrieveUpdateDestroyAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)
