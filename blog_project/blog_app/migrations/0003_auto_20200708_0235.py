# Generated by Django 3.0.8 on 2020-07-07 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_app', '0002_auto_20200708_0139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
