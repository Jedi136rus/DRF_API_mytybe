from rest_framework import serializers

from .models import Post, Comment, Follow


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        many=False,
        read_only=True,
        )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        fields = ('id', 'author', 'post', 'text', 'created')
        model = Comment


class FollowSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        fields = ('user', 'author')
        model = Follow
