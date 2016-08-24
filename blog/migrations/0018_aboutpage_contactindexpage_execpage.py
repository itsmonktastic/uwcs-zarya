# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-24 19:39
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import wagtail.wagtailcore.blocks
import wagtail.wagtailcore.fields
import wagtail.wagtaildocs.blocks
import wagtail.wagtailimages.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0029_unicode_slugfield_dj19'),
        ('blog', '0017_auto_20160815_0847'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('body', wagtail.wagtailcore.fields.StreamField((('h2', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h3', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('h4', wagtail.wagtailcore.blocks.CharBlock(classname='title', icon='title')), ('paragraph', wagtail.wagtailcore.blocks.RichTextBlock(icon='pilcrow')), ('image', wagtail.wagtailimages.blocks.ImageChooserBlock()), ('pullquote', wagtail.wagtailcore.blocks.StructBlock((('quote', wagtail.wagtailcore.blocks.TextBlock('quote title')), ('attribution', wagtail.wagtailcore.blocks.CharBlock())))), ('document', wagtail.wagtaildocs.blocks.DocumentChooserBlock(icon='doc-full-inverse')), ('code', wagtail.wagtailcore.blocks.StructBlock((('language', wagtail.wagtailcore.blocks.ChoiceBlock(choices=[('bash', 'Bash/Shell'), ('c', 'C'), ('cmake', 'CMake'), ('cpp', 'C++'), ('csharp', 'C#'), ('css', 'CSS'), ('go', 'Go'), ('haskell', 'Haskell'), ('haxe', 'Haxe'), ('html', 'HTML'), ('java', 'Java'), ('js', 'JavaScript'), ('json', 'JSON'), ('kotlin', 'Kotlin'), ('lua', 'Lua'), ('make', 'Makefile'), ('perl', 'Perl'), ('perl6', 'Perl 6'), ('php', 'PHP'), ('python', 'Python'), ('python3', 'Python 3'), ('ruby', 'Ruby'), ('sql', 'SQL'), ('swift', 'Swift'), ('xml', 'XML')])), ('code', wagtail.wagtailcore.blocks.TextBlock()))))))),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ContactIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ExecPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
    ]
