# Generated by Django 3.1.12 on 2021-08-28 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0002_auto_20210818_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='body',
            field=models.CharField(default=None, max_length=1555),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='blog'),
        ),
    ]
