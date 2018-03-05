# refer
# https://docs.djangoproject.com/en/2.0/howto/custom-template-tags/
from django import template
from django.db.models import Count
# Custom Filter templatetags
from django.utils.safestring import mark_safe
import markdown

# To be a valid tag library, the module must contain a module-level variable named
# register that is a template.Library instance, in which all the tags and filters are registered.
register = template.Library()

from ..models import Post


@register.simple_tag
def total_post():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.assignment_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
    # https://docs.djangoproject.com/en/2.0/ref/utils/
