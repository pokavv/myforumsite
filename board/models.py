from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50)
    post_image = models.ImageField(blank=True, null=True)
    contents = models.TextField()
    dt_created = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name='수정일', auto_now=True)
    
    # postname을 Post Object 대신 나오게함
    def __str__(self):
        return self.postname