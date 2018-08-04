from adminsortable2.admin import SortableAdminMixin
from modeltranslation.admin import TranslationAdmin


class SortableTranslationAdmin(SortableAdminMixin, TranslationAdmin):
    pass
