from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericRelation
from django.db import models

from likes.models import Like

User = get_user_model()


class Posts(models.Model):
    """Модель новости"""
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата новости',
        db_index=True
    )
    title = models.CharField(
        max_length=100,
        verbose_name='Заголовок новости',
        help_text='Введите заголовок новости')
    text = models.TextField(
        verbose_name='Текст новости',
        help_text='Введите текст новости'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор новости'
    )
    likes = GenericRelation(Like)


    class Meta:
        ordering = ("-pub_date",)
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'

    def __str__(self):
        return self.text[:15]

    @property
    def total_likes(self):
        return self.likes.count()


class Comment(models.Model):
    """Модель комментария"""
    post = models.ForeignKey(
        Posts,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='comments',
        verbose_name='Новость, к которой оставлен комментарий'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    text = models.TextField(
        verbose_name='Текст комментария',
        help_text='Введите текст комментария'
    )
    created = models.DateTimeField(
        verbose_name='Дата публикации комментария',
        auto_now_add=True
    )


    class Meta:
        ordering = ['-created']
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text
