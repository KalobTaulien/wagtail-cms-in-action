from wagtail.admin.panels import FieldPanel
from wagtail.core.models import Page
from wagtail.core import blocks
from wagtail.core.fields import StreamField
from wagtail.images.blocks import ImageChooserBlock


class BlogIndexPage(Page):
    max_count = 1
    subpage_types = ['blog.BlogPostPage']


class BlogPostPage(Page):
    parent_page_types = ['blog.BlogIndexPage']

    body = StreamField([
        ("title", blocks.CharBlock(
            form_classname="full title",
            template="blocks/title_block.html"
        )),
        ("richtext", blocks.RichTextBlock()),
        ("image", ImageChooserBlock())
    ], blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel('body')
    ]
