from django.db import models
import random
from django.conf import settings
from django.db.models import Q

User = settings.AUTH_USER_MODEL


class TweetLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tweet = models.ForeignKey('Tweet', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)

class TweetQuerySet(models.QuerySet):
    def by_username(self, username):
        return self.filter(user__username__iexact=username)

    def feed(self, user):
        profile_exist = user.following.exists()
        followed_users_id = []
        if profile_exist :
            followed_users_id = user.following.all().values_list("user__id", flat=True) # [x.user.id for x in profiles]
        # followed_users_id.append(user.id)
        return self.filter(
                            Q(user__id__in=followed_users_id) |
                            Q(user=user)
                    ).distinct().order_by("-timestamp") # Model.objects

class TweetManager(models.Manager):
    def get_queryset(self, *args, **kwargs) :
        return TweetQuerySet(self.model, using=self._db)

    def feed(self, user) :
        return self.get_queryset().feed(user)

class Tweet(models.Model):
    # id = models.AutoField(primary=True)
    parent = models.ForeignKey("self", null=True, on_delete=models.SET_NULL)
    # many users can many tweets
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="tweets")
    likes = models.ManyToManyField(
        User, related_name='tweet_user', blank=True, through=TweetLike)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = TweetManager()

    class Meta:
        ordering = ["-id"]

    # def __str__(self):
    #     return self.content

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
