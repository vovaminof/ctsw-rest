from modeltranslation.translator import register, TranslationOptions

from resource.models import Category, Resource


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ("name",)


@register(Resource)
class ResourceTranslationOptions(TranslationOptions):
    fields = ("name",)
