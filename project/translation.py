from modeltranslation.translator import register, TranslationOptions

from project.models import Project


@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ("name", "summary", "content")
