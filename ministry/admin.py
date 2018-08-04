from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from ministry.models import Ministry


admin.site.register(Ministry, TranslationAdmin)
