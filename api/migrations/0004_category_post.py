# Generated by Django 3.2.12 on 2023-08-14 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='post',
            field=models.ManyToManyField(to='api.Post'),
        ),
    ]
