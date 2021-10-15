from django.db import models
import random
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Tweet(models.Model):
    # id = models.AutoField(primary=True)

    # many users can many tweets
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)
    image = models.FileField(upload_to='images/', blank=True, null=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.content

    def serialize(self):
        return {
            "id": self.id,
            "content": self.content,
            "likes": random.randint(0, 200),
        }
