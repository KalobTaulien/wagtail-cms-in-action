from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.admin.panels import FieldPanel, InlinePanel
from wagtail.core.models import Page, Orderable


class ProductIndexPage(Page):
    max_count = 1
    subpage_types = ['products.ProductDetailPage']


class ProductDetailPage(Page):
    parent_page_types = ['products.ProductIndexPage']
    subpage_types = []

    content_panels = Page.content_panels + [
        InlinePanel(
            "product_images",
            max_num=5,
            min_num=1,
            label="Product Images"
        ),
    ]


class ProductImages(Orderable):
    page = ParentalKey('products.ProductDetailPage', related_name="product_images")
    image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+"
    )
    alt_text = models.CharField(max_length=100, blank=False, default='')
    short_description = models.CharField(max_length=255, blank=True)

    panels = [
        FieldPanel("image"),
        FieldPanel("alt_text"),
        FieldPanel("short_description"),
    ]
