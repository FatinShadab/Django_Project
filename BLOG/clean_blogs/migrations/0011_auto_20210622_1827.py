# Generated by Django 3.2.4 on 2021-06-22 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clean_blogs', '0010_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(verbose_name='content'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='img',
            field=models.ImageField(upload_to='media/store/blog_imgs', verbose_name='img'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='short_desc',
            field=models.CharField(max_length=550, unique=True, verbose_name='sub-heading'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='slug',
            field=models.SlugField(max_length=200, unique=True, verbose_name='slug'),
        ),
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=250, unique=True, verbose_name='title'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='desc',
            field=models.TextField(verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='short_desc',
            field=models.CharField(max_length=550, verbose_name='ShortDesc'),
        ),
        migrations.AlterField(
            model_name='projects',
            name='url',
            field=models.URLField(verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='socialurl',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Platfrom'),
        ),
        migrations.AlterField(
            model_name='socialurl',
            name='url',
            field=models.URLField(verbose_name='Url'),
        ),
        migrations.AlterField(
            model_name='video',
            name='title',
            field=models.CharField(max_length=150, verbose_name='Title'),
        ),
    ]
