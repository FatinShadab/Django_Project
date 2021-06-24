# Generated by Django 3.2.4 on 2021-06-18 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clean_blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='')),
                ('file', models.FileField(upload_to=None, verbose_name='')),
            ],
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(verbose_name=''),
        ),
    ]
