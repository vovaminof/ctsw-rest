from modeltranslation.translator import register, TranslationOptions

from ministry.models import Ministry


@register(Ministry)
class MinistryTranslationOptions(TranslationOptions):
    fields = ("name", "content",)
