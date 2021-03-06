from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=264)
    text=models.TextField()
    picture=models.ImageField(upload_to="post_pics",blank=True)
    create_date=models.DateTimeField(default=timezone.now)
    publish_date=models.DateTimeField(blank=True,null=True)

    def publish(self):
        self.publish_date=timezone.now()
        self.save()
    def approve_comments(self):
        return self.comments.filter(approve_comments=True)
    def get_absolute_url(self):
        return reverse("post_detail",kwargs={'pk':self.pk})
    def __str__(self):
        return self.title
class Comment(models.Model):
    post=models.ForeignKey('myapp.Post',related_name='comments',on_delete=models.CASCADE)
    author=models.CharField(max_length=264)
    text=models.TextField()
    create_date=models.DateTimeField(default=timezone.now)
    approve_comments=models.BooleanField(default=False)

    def approve(self):
        self.approve_comments=True
        self.save()
    def __str__(self):
        return self.text
