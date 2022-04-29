from django import template
from home.models import HomePage

register = template.Library()


@register.simple_tag
def global_nav_items():
    homepage = HomePage.objects.first()
    return homepage.get_children().in_menu().live()
