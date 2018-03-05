from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from taggit.managers import TaggableManager
# wysiwyg editor
from tinymce.models import HTMLField

# Create your models here.


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='published')


class Category(models.Model):
    category_title = models.CharField(max_length=250)
    category_slug = models.SlugField(max_length=250, unique=True)
    category_parent = models.ForeignKey('self', blank=True, null=True, related_name='subcategory')
    category_description = HTMLField()
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return self.category_title


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    category = models.ForeignKey(Category, related_name='category')
    author = models.ForeignKey(User, related_name='blog_posts')
    # body = models.TextField()
    body = HTMLField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    # custom manager(to perform query)
    # https://docs.djangoproject.com/en/1.8/topics/db/managers/
    objects = models.Manager()  # the default manager
    published = PublishedManager()  # custom manager
    tags = TaggableManager()

    class Meta:
        ordering = ('-publish',)  # telling django to sort data by publish in descending order when quried the db

    # default human readable representation of the object
    def __str__(self):
        return self.title

    # canonical url
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
            self.publish.year,
            self.publish.strftime('%m'),
            self.publish.strftime('%d'),
            self.slug
        ])


class Comment(models.Model):
    # django many to one relationship
    # https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_one/
    post = models.ForeignKey(Post, related_name='comments')
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('created',)

    def __str__(self):
        return 'Commented by {} on {}'.format(self.name, self.post)
