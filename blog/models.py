from wagtail.core.models import Page


class BlogIndexPage(Page):
    max_count = 1
    subpage_types = ['blog.BlogPostPage']


class BlogPostPage(Page):
    parent_page_types = ['blog.BlogIndexPage']
