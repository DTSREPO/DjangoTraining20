# Generated by Django 2.2 on 2020-06-30 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0002_auto_20200630_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.CharField(max_length=15, verbose_name='Age'),
        ),
        migrations.AlterField(
            model_name='student',
            name='cls',
            field=models.CharField(max_length=150, verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='student',
            name='gender',
            field=models.CharField(max_length=30, verbose_name='Gender'),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Student Name'),
        ),
        migrations.AlterField(
            model_name='student',
            name='roll',
            field=models.IntegerField(verbose_name='Roll'),
        ),
    ]