from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from about.models import About


admin.site.register(About, TranslationAdmin)
