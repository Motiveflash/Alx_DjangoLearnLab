# Generated by Django 5.1.4 on 2024-12-15 15:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_published_date_alter_comment_author_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-created_at']},
        ),
    ]
