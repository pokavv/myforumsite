# Generated by Django 2.2 on 2023-04-10 14:56

import board.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(error_messages={'unique': '중복된 제목은 등록할 수 없습니다!'}, max_length=50, unique=True)),
                ('post_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('contents', models.TextField(validators=[django.core.validators.MinLengthValidator(10, '너무 짧습니다. 10자 이상 적어주세요.'), board.validators.validate_symbols])),
                ('dt_created', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('dt_modified', models.DateTimeField(auto_now=True, verbose_name='수정일')),
            ],
        ),
    ]
