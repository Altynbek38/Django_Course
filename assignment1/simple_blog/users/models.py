from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    bio = models.TextField()
    profile_picture = models.ImageField(upload_to='images/')

    class Meta():
        verbose_name = "Profile"
        verbose_name_plural = "Profiles"

    def __str__(self):
        return f"user: {self.user}, bio: {self.bio}"
    
    def to_json(self):
        return {
            "user": self.user,
            "bio": self.bio,
            "profiele_picture": self.profile_picture
        }

class Follow(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    following = models.ForeignKey(User, on_delete=models.CASCADE, related_name="following")

    class Meta():
        verbose_name = "Follow"
        verbose_name_plural = "Follows"
    
    def __str__(self):
        return f"follower: {self.follower}, following: {self.following}"

    def to_json(self):
        return {
            "follower": self.follower,
            "following": self.following
        } 