from django.core.management.base import BaseCommand
from taggit.models import Tag


class Command(BaseCommand):
    def handle(self, *args, **options):
        for tag in Tag.objects.all():
            if tag.taggit_taggeditem_items.count() == 0:
                print("Removing: {}".format(tag))
                tag.delete()
