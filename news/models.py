from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from ckeditor.fields import RichTextField
from django.template.defaultfilters import truncatechars
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime
from bs4 import BeautifulSoup

date = datetime.datetime.now().strftime('%b-%d-%G')

class Category(models.Model):
    name = models.CharField(max_length=255)
    cover_image = CloudinaryField('cover_image', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"

class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Tags"

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    facebook_url = models.URLField(blank=True, null=True)
    twitter_url = models.URLField(blank=True, null=True)
    instagram_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    youtube_url = models.URLField(blank=True, null=True)
    tiktok_url = models.URLField(blank=True, null=True)
    profile_picture = CloudinaryField('profile_picture', null=True, blank=True)

    def __str__(self):
        return self.user.username
        
    class Meta:
        verbose_name_plural = "Authors"

    def can_edit_social_media(self):
        return self.user.is_superuser

class News(models.Model):
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    title = models.CharField(max_length=255)
    cover_image_url  = CloudinaryField('cover_image', null=True, blank=True) #models.ImageField(upload_to='uploads/') #
    text = RichTextField()  # Use RichTextField instead of TextField
    view_count = models.PositiveIntegerField(default=0, db_index=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    text_preview = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "News"

@receiver(pre_save, sender=News)
def create_text_preview(sender, instance, **kwargs):
    soup = BeautifulSoup(instance.text, 'html.parser')
    paragraphs = soup.find_all('p')

    text_preview = ' '.join([p.get_text() for p in paragraphs])

    instance.text_preview = truncatechars(text_preview, 200)

class DecorativeImages(models.Model):
    image  = CloudinaryField('decorative_image', null=True, blank=True)

    class Meta:
        verbose_name_plural = "Decorative Images"