from django.conf import settings
from rest_framework import serializers
from rest_framework.decorators import action
from .models import Tweet, TweetLike
from profiles.serializers import PublicProfileSerializer

MAX_TWEET_LENGTH = settings.MAX_TWEET_LENGTH
TWEET_ACTION_OPTIONS = settings.TWEET_ACTION_OPTIONS


class TweetActionSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    action = serializers.CharField()
    content = serializers.CharField(allow_blank=True, required=False)

    def validated_action(self, value):
        value = value.lower().strip()
        if not value in TWEET_ACTION_OPTIONS:
            raise serializers.ValidationError("잘못된 경로 입니다.")
        return value


class TweetCreateSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True) # serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Tweet
        fields = ["user", "id", "content", "likes", "timestamp"]

    # def get_user(self, obj) :
    #     return obj.user.id

    def get_likes(self, obj):
        return obj.likes.count()

    def validate_content(self, value):
        if len(value) > MAX_TWEET_LENGTH:
            raise serializers.ValidationError("해당 글의 길이가 너무 깁니다.")
        return value

class TweetSerializer(serializers.ModelSerializer):
    user = PublicProfileSerializer(source='user.profile', read_only=True) # user = serializers.SerializerMethodField(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    parent = TweetCreateSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = ["user", "id", "content", "likes", "is_retweet", "parent", "timestamp"]

    # def get_user(self, obj) :
    #     return obj.user.id

    def get_likes(self, obj):
        return obj.likes.count()