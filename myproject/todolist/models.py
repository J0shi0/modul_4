from django.db import models


class Task(models.Model):
    STATUS_DRAFT = 'DRAFT'
    STATUS_PUBLISHED = 'PUBLISHED'

    STATUSES = (
        (STATUS_DRAFT, 'Черновик'),
        (STATUS_PUBLISHED, 'Опубликована')
    )

    title = models.CharField(max_length=300, verbose_name='Тема задачи')
    description = models.CharField(max_length=300, null=True, blank=True, verbose_name='Описания')

    status = models.CharField(choices=STATUSES, default=STATUS_DRAFT, verbose_name='Статус', max_length=15)

    deadline_date = models.DateField(null=True, blank=True)
    author = models.CharField(max_length=200, default='admin')
    tags = models.ManyToManyField('Tag', verbose_name='тэг', related_name='tasks')

    class Meta:
        verbose_name = 'задача'
        verbose_name_plural = 'задачи'

    def __str__(self):
        return self.title


class Comment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return f'Comment:({self.text}) - created on {self.created_at}'


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'тег'
        verbose_name_plural = 'теги'

    def __str__(self):
        return self.name
