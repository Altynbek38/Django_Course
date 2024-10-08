from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta():
        verbose_name = "Post"
        verbose_name_plural = "Posts"

    def __str__(self):
        return f"title: {self.title}, content: {self.content}, created_at: {self.created_at}, author: {self.author}"
    
    def to_json(self):
        return {
            "title": self.title,
            "content": self.content,
            "created_at": self.created_at,
            "author": self.author
        }

class Comment(models.Model):
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta():
        verbose_name = "Comment"
        verbose_name_plural = "Comments"

    def __str__(self):
        return f"content: {self.content}, created_at: {self.created_at}, post: {self.post}, author: {self.author}"
    
    def to_json(self):
        return {
            "content": self.content,
            "created_at": self.created_at,
            "post": self.post,
            "author": self.author
        }