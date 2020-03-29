from django import template
from lost.models import KindL

register = template.Library()

@register.inclusion_tag('/cats.html')
def get_category_list():
    return {'cats': KindL.objects.all()}