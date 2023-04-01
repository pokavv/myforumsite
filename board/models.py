from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_symbols

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=50, unique=True, 
                            error_messages={'unique': '중복된 제목은 등록할 수 없습니다!'})
    post_image = models.ImageField(blank=True, null=True)
    contents = models.TextField(validators=[MinLengthValidator(10, '너무 짧습니다. 10자 이상 적어주세요.'),
                                            validate_symbols])
    dt_created = models.DateTimeField(verbose_name='작성일', auto_now_add=True)
    dt_modified = models.DateTimeField(verbose_name='수정일', auto_now=True)
    
    # postname을 Post Object 대신 나오게함
    def __str__(self):
        return self.title