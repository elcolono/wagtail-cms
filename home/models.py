from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField


class HomePage(Page):
    body = RichTextField(blank=True)
    
    content_panels = Page.content_panels + [
        FieldPanel('body', classname="full"),
    ]