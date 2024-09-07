from django.urls import path, include
from .views import base, about_us

from rest_framework.routers import DefaultRouter
from .views import TaskViewSet, TagViewSet, CommentListCreateAPIVIew, CommentRetrieveUpdateDestroyAPI

router = DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'tags', TagViewSet)

urlpatterns = [
    path('', base, name='base'),
    path('about_us', about_us, name='about_us'),
    path('', include(router.urls)),
    path(r'comments/', CommentListCreateAPIVIew.as_view()),
    path(r'comments/<int:pk>/', CommentRetrieveUpdateDestroyAPI.as_view())
    ]