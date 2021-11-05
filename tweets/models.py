from django.db import models
import random
from django.conf import settings
from django.db.models.base import Model

User = settings.AUTH_USER_MODEL


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)


class Tweet(models.Model):
    # id = models.AutoField(primary=True)

    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    # many users can many tweets
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(
        User, related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.content

    @property
    def is_retweet(self):
        return self.parent != None


    def serialize(self):
        '''
        없어도 돼요~
        '''
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200),
        }
