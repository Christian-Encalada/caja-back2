# Generated by Django 4.2.3 on 2023-07-19 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hermanast', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='emmail',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
