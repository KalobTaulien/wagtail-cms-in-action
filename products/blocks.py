from wagtail.core import blocks


class TitleAndSubtitleBlock(blocks.StructBlock):
    title = blocks.CharBlock(max_length=100, required=True)
    subtitle = blocks.CharBlock(max_length=250, required=False)

    class Meta:
        template = "blocks/title_and_subtitle_block.html"
        icon = "edit"
        label = "Title & Text"
