from django import template
from django.core.cache import cache

from home.models import HomePage

register = template.Library()


@register.simple_tag
def global_nav_items():
    CACHE_NAME = "MENU_PAGES"
    if cache.get(CACHE_NAME):
        menu_pages = cache.get(CACHE_NAME)
    else:
        homepage = HomePage.objects.first()
        menu_pages = homepage.get_children().in_menu().live()
        cache.set(CACHE_NAME, menu_pages, 25200)
    return menu_pages
