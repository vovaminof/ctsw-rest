from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from project.models import Project

admin.site.register(Project, TranslationAdmin)
