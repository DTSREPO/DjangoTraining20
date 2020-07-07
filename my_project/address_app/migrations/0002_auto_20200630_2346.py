# Generated by Django 2.2 on 2020-06-30 17:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('address_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='district',
            name='description',
        ),
        migrations.AddField(
            model_name='district',
            name='population',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name='Population'),
            preserve_default=False,
        ),
    ]