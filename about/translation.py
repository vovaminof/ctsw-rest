from modeltranslation.translator import register, TranslationOptions

from about.models import About


@register(About)
class AboutTranslationOptions(TranslationOptions):
    fields = ("name", "summary", "content")
