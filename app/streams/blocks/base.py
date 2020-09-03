from django import forms
from django.utils.encoding import force_text
from django.utils.text import slugify
from wagtail.core.blocks import StructBlock, FieldBlock, ChoiceBlock
from wagtail_color_panel.blocks import NativeColorBlock


class HashBlock(FieldBlock):
    """ Hash values which will allow sections to be automatically linked to using URL hashes
    e.g. link to a page at a particular section could be https://your-site.com/your-page-slug/#your-section-hash
    Can be blank, in which case no hash should be generated for the section.
    This Block is essentially a CharBlock with a custom clean() method.
    """

    def __init__(self, required=True, help_text=None, max_length=None, min_length=None, **kwargs):
        self.field = forms.CharField(required=required, help_text=help_text, max_length=max_length, min_length=min_length)
        super().__init__(**kwargs)

    def get_searchable_content(self, value):
        return [force_text(value)]

    def clean(self, value):
        if value:
            return slugify('section-' + force_text(value), allow_unicode=False)
        return value


class SectionBlock(StructBlock):
    """ A StructBlock, but with a `hash` field that can be used to generate links to sections of page content
    """
    hash = HashBlock(
        required=False,
        max_length=80,
        label='Hash',
        help_text="Allow navigation to this section within a page. e.g. 'team' allows navigation to /http://your-site.com/#team",
        classname=(
            'block_setting_field'
        ),
    )
    background_type = ChoiceBlock(
        required=False,
        choices=[
            ('transparent', 'Transparent'),
            ('solid', 'Solid Color'),
            ('gradient', 'Gradient Color'),
            ('image', 'Background Image'),
        ],
        icon='pick',
        help_text='Transparent background will use the background-color "page settings".',
        classname='block_setting_choice',
    )
    background_color = NativeColorBlock(
        default="#000000",
        classname='block_setting_sub solid gradient',
        required=False,

    )
    background_color_2 = NativeColorBlock(
        default="#000000",
        classname='block_setting_sub gradient',
        required=False,
    )
    # background_color_3 = NativeColorBlock(
    #     default="#000000",
    #     classname=(
    #         'block_settings_field show_if'
    #     )
    # )