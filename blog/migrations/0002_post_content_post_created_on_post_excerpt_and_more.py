# Generated by Django 4.2.17 on 2024-12-13 23:48

from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='post',
            name='created_on',
            field=models.DateTimeField(
                auto_now_add=True,
                default=datetime.datetime.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='status',
            field=models.IntegerField(
                choices=[(0, 'Draft'), (1, 'Published')],
                default=0,
            ),
        ),
    ]