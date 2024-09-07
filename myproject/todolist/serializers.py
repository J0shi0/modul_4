from rest_framework import serializers
from .models import Task, Comment, Tag


class CommentSerializer(serializers.ModelSerializer):  # создаем класс наследник от базового класса сериализатор на
    # основе модели
    class Meta:
        model = Comment  # указываем модель, для которой будут сериализоваться и десериализоваться данные
        fields = ['task',
                  'text']  # указываем набор полей, с которыми будем работать при сериализации и десериализации


class TagSerializer(serializers.ModelSerializer):  # создаем класс наследник от базового класса сериализатор на
    # основе модели
    class Meta:
        model = Tag  # указываем модель, для которой будут сериализоваться и десериализоваться данные
        fields = ['id', 'name']  # указываем набор полей, с которыми будем работать при сериализации и десериализации


class TaskSerializer(serializers.ModelSerializer):  # создаем класс наследник от базового класса сериализатор на
    # основе модели
    comments_count = serializers.SerializerMethodField(read_only=True)

    tags = TagSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    class Meta:
        model = Task  # указываем модель, для которой будут сериализоваться и десериализоваться данные
        fields = ['title', 'description', 'status', 'deadline_date', 'comments_count', 'comments', 'tags']
        # указываем набор полей, с которыми будем работать при сериализации и десериализации

    def get_comments_count(self, obj): # выполняет подсчет комментариев для соответствущей задачи
        return obj.comments.all().count()
