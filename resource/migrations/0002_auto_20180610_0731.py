# Generated by Django 2.0.5 on 2018-06-10 04:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('order',), 'verbose_name_plural': 'categories'},
        ),
        migrations.AlterModelOptions(
            name='resource',
            options={'verbose_name_plural': 'resources'},
        ),
    ]
