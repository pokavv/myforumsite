from django.db import models

# Create your models here.

class Post(models.Model):
    postname = models.CharField(max_length=50)
    post_image = models.ImageField(blank=True, null=True)
    contents = models.TextField()
    
    # postname을 Post Object 대신 나오게함
    def __str__(self):
        return self.postname