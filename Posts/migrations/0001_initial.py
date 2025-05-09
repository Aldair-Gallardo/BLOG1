# Generated by Django 5.2 on 2025-04-25 01:56

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('title', models.CharField(max_length=200)),
                ('subtitulo', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('imagen_portada', models.ImageField(blank=True, default='', null=True, upload_to='')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
            ],
        ),
    ]
