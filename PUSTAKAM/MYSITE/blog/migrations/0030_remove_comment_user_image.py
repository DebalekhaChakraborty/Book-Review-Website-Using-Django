# Generated by Django 2.2.2 on 2019-06-25 20:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_comment_user_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='user_image',
        ),
    ]
