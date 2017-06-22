from __future__ import unicode_literals

from django.db import models
from ..reg.models import Users

class Post(models.Model):
    user_id=models.ForeignKey(Users, related_name="all_posts")
    content=models.TextField(max_length=1000)
    user_likes = models.ManyToManyField(Users, related_name="post_likes")
    total_likes=models.IntegerField(default=0)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.content

# class Like(models.Model):
#     post_id=models.ForeignKey(Post, related_name="all_likes")
#     user_id=models.ForeignKey(Users, related_name="all_likes")
#     created_at=models.DateTimeField(auto_now_add=True)
#     updated_at=models.DateTimeField(auto_now=True)
#     def __str__(self):
#         return self.id
