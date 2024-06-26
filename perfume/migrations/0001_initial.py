# Generated by Django 5.0.3 on 2024-03-14 17:57

import django.db.models.deletion
import taggit.managers
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
    ]

    operations = [
        migrations.CreateModel(
            name='Accord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accord', models.CharField(max_length=200, unique=True)),
            ],
            options={
                'ordering': ['accord'],
            },
        ),
        migrations.CreateModel(
            name='Designer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('logo', models.URLField(max_length=300)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=200, unique=True)),
                ('image', models.URLField(max_length=300)),
            ],
            options={
                'ordering': ['note'],
            },
        ),
        migrations.CreateModel(
            name='Perfume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('image', models.URLField(max_length=300)),
                ('summary', models.TextField(help_text='Enter a brief description of the perfume', max_length=1000)),
                ('rating', models.IntegerField(default=1)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('accords', models.ManyToManyField(to='perfume.accord')),
                ('base_notes', models.ManyToManyField(related_name='base_notes', to='perfume.note')),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='perfume.designer')),
                ('heart_notes', models.ManyToManyField(related_name='heart_notes', to='perfume.note')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
                ('top_notes', models.ManyToManyField(related_name='top_notes', to='perfume.note')),
            ],
        ),
    ]
