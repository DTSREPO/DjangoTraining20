# Generated by Django 2.2 on 2020-06-30 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='District Name')),
                ('description', models.TextField(max_length=400, verbose_name='District Intro')),
                ('area', models.CharField(max_length=50, verbose_name='Area')),
            ],
        ),
    ]
