from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from blog.models import Post, Author

admin.site.register(Post, TranslationAdmin)
admin.site.register(Author, TranslationAdmin)
