from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from resource.models import Category, Resource
from utils.admin import SortableTranslationAdmin


admin.site.register(Category, SortableTranslationAdmin)
admin.site.register(Resource, TranslationAdmin)
