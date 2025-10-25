from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
# Create your models here.

def validate_video_extension(value):
    import os
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.mp4', '.mov', '.webm']
    if ext not in valid_extensions:
        raise ValidationError("Unsupported file type. Only mp4, mov and webm files are allowed")

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    images = models.ImageField(upload_to="posts/photos/", blank=True, null=True)
    videos = models.FileField(upload_to="posts/videos/", blank=True, null=True, validators=[validate_video_extension])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="liked_post", blank=True)

#Keeping track of number of likes

    def number_of_likes(self):
        return self.likes.count()

    def __str__(self):
        return f'{self.user.username} - {self.text[:10]}'
    
class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=250)
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (self.name)
    