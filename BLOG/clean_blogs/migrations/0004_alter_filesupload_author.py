# Generated by Django 3.2.4 on 2021-06-19 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clean_blogs', '0003_auto_20210618_2217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filesupload',
            name='author',
            field=models.CharField(max_length=100, verbose_name=''),
        ),
    ]
