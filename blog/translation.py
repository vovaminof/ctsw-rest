from modeltranslation.translator import register, TranslationOptions

from blog.models import Author, Post


@register(Author)
class AuthorTranslationOptions(TranslationOptions):
    fields = ("name", "about",)


@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ("title", "text",)
