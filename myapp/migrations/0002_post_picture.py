# Generated by Django 3.0.3 on 2021-02-12 03:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='picture',
            field=models.ImageField(blank=True, upload_to='post_pics'),
        ),
    ]
