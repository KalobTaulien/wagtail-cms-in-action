from wagtail.core.models import Page


class ProductIndexPage(Page):
    max_count = 1
    subpage_types = ['products.ProductDetailPage']


class ProductDetailPage(Page):
    parent_page_types = ['products.ProductIndexPage']
    subpage_types = []
