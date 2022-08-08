from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Posts, Comment
from likes import service as likes_services

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """Сериализатор новостей."""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Posts

    def get_is_fan(self, obj) -> bool:
        """Ставил ли пользователь лайк."""
        user = self.context.get('request').user
        return likes_services.is_fan(obj, user)


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор комментариев."""
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
