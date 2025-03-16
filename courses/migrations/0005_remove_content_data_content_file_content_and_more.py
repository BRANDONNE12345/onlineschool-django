# Generated by Django 5.1.7 on 2025-03-16 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0004_remove_chapter_content_content_forum_message_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='data',
        ),
        migrations.AddField(
            model_name='content',
            name='file_content',
            field=models.FileField(blank=True, null=True, upload_to='contents/'),
        ),
        migrations.AddField(
            model_name='content',
            name='text_content',
            field=models.TextField(blank=True, null=True),
        ),
    ]
