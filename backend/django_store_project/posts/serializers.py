from rest_framework import serializers

from .models import Post, PostReply
# from store.serializers import GamePostSerializer
from users.serializers import UserPostSerializer


class PostReplySerializer(serializers.ModelSerializer):

    # game = GamePostSerializer(read_only=True, many=False)
    author = UserPostSerializer(read_only=True, many=False)

    class Meta:
        model = PostReply
        fields = ('author', 'created_at', 'content')


class PostSerializer(serializers.ModelSerializer):

    # game = GamePostSerializer(read_only=True, many=False)
    author = UserPostSerializer(read_only=True, many=False)
    get_replies = PostReplySerializer(many=True)

    class Meta:
        model = Post
        fields = ('author', 'created_at', 'content', 'get_replies')