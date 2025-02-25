from django.db import models

from wagtail.admin.edit_handlers import (
    FieldPanel,
    InlinePanel,
    StreamFieldPanel
)
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet

from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel

from wagtailio.features.blocks import FeatureIndexPageBlock


class Bullet(Orderable, models.Model):
    snippet = ParentalKey('features.FeatureAspect', related_name='bullets')
    title = models.CharField(max_length=255)
    text = RichTextField()

    panels = [
        FieldPanel('title'),
        FieldPanel('text')
    ]


@register_snippet
class FeatureAspect(ClusterableModel):
    title = models.CharField(max_length=255)
    video_url = models.URLField(blank=True)
    screenshot = models.ForeignKey(
        'images.WagtailIOImage',
        models.SET_NULL,
        null=True,
        blank=True,
        related_name='+'
    )

    def __str__(self):
        return self.title

    panels = [
        FieldPanel('title'),
        InlinePanel('bullets', label="Bullets"),
        ImageChooserPanel('screenshot'),
        FieldPanel('video_url'),
    ]


class FeaturePageFeatureAspect(Orderable, models.Model):
    page = ParentalKey('features.FeatureDescription', related_name='feature_aspects')
    feature_aspect = models.ForeignKey(
        'features.FeatureAspect',
        models.CASCADE,
        related_name='+'
    )

    panels = [
        SnippetChooserPanel('feature_aspect')
    ]


@register_snippet
class FeatureDescription(ClusterableModel):
    title = models.CharField(max_length=255)
    introduction = models.CharField(max_length=255, blank=True)
    documentation_link = models.URLField(max_length=255, blank=True)
    panels = [
        FieldPanel('title'),
        FieldPanel('introduction'),
        FieldPanel('documentation_link'),
        InlinePanel('feature_aspects', label="Feature Aspects"),
    ]

    def __str__(self):
        return self.title


class FeatureIndexPageMenuOption(models.Model):
    page = ParentalKey('features.FeatureIndexPage',
                       related_name='secondary_menu_options')
    link = models.ForeignKey(
        'wagtailcore.Page',
        models.CASCADE,
        related_name='+'
    )
    label = models.CharField(max_length=255)


class FeatureIndexPage(Page):
    body = StreamField(FeatureIndexPageBlock())

    content_panels = Page.content_panels + [
        StreamFieldPanel('body'),
    ]
