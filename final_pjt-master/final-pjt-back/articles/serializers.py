from rest_framework import serializers
from .models import Article, Comment


class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)


class ArticleSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Article
        fields = '__all__'
        read_only_fields = ('user',)


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ('article', 'user')
