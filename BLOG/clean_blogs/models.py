from django.db import models
from django.contrib.auth.models import User
from embed_video.fields import EmbedVideoField


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)

# Create your models here.
class Contact(models.Model):
        name = models.CharField(("Name"), max_length=50)
        email = models.EmailField(("Email"), max_length=254)
        desc = models.TextField(("Message"))
        date = models.DateField("Date")

        def __str__(self):
            return self.name

class SocialUrl(models.Model):
        name = models.CharField(("Platfrom"), max_length=50)
        url = models.URLField(("Url"), max_length=200)

        def __str__(self):
            return self.name
        

class BlogPost(models.Model):
        title = models.CharField(("title"), max_length=250, unique=True)
        slug = models.SlugField(("slug"), max_length=200, unique=True)
        short_desc = models.CharField(("sub-heading"), max_length=550, unique=True)
        img = models.ImageField(("img"), upload_to='media/store/blog_imgs', height_field=None, width_field=None, max_length=None)
        author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_pots')
        updated_on = models.DateTimeField(auto_now_add=True)
        content = models.TextField(("content"))
        created_on = models.DateTimeField(auto_now_add=True)
        status = models.IntegerField(choices=STATUS, default=0)
        
        @property
        def file_url(self):
            if self.img and hasattr(self.img, 'url'):
                return self.img.url

        class Meta:
            ordering = ['-created_on']

        def __str__(self):
            return self.title
        

class FilesUpload(models.Model): 
    name = models.CharField((""), max_length=50)
    author = models.CharField((""), max_length=100)
    file = models.FileField((""), upload_to='media/store/pdfs', max_length=150)

    @property
    def file_url(self):
        if self.file and hasattr(self.file, 'url'):
            return self.file.url
    
    def __str__(self):
        return self.name


class Projects(models.Model):
    name = models.CharField(("Name"), max_length=50)
    short_desc = models.CharField(("ShortDesc"), max_length=550)
    url = models.URLField(("Url"), max_length=200)

    def __str__(self):
        return self.name

    
class Video(models.Model):
    title = models.CharField(("Title"), max_length=150)
    url = EmbedVideoField()
    added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
         ordering = ['-added']
    
    
    