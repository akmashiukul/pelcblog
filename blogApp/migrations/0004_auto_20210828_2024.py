# Generated by Django 3.1.12 on 2021-08-28 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_auto_20210828_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.TextField(default=None, max_length=1555),
        ),
    ]