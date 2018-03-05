# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.utils.timezone
import tinymce.models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category_title', models.CharField(default=b'category', max_length=250)),
                ('category_slug', models.SlugField(unique=True, max_length=250)),
                ('category_description', tinymce.models.HTMLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('category_parent', models.ForeignKey(related_name='subcategory', to='blog.Category')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(max_length=254)),
                ('body', models.TextField()),
                ('active', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('created',),
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date=b'publish')),
                ('body', tinymce.models.HTMLField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default=b'draft', max_length=10, choices=[(b'draft', b'Draft'), (b'published', b'Published')])),
                ('author', models.ForeignKey(related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
                ('category', models.ForeignKey(verbose_name=b'Category', to='blog.Category')),
                ('tags', taggit.managers.TaggableManager(to='taggit.Tag', through='taggit.TaggedItem', help_text='A comma-separated list of tags.', verbose_name='Tags')),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(related_name='comments', to='blog.Post'),
        ),
    ]
