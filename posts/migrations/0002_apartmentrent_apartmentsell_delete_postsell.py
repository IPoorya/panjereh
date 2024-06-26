# Generated by Django 5.0.1 on 2024-01-04 13:41

import django.db.models.deletion
import posts.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentRent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('description', models.TextField(max_length=2047)),
                ('meterage', models.FloatField()),
                ('room', models.IntegerField()),
                ('build', models.IntegerField()),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('total_floors', models.IntegerField(blank=True, null=True)),
                ('unit_per_floor', models.IntegerField(blank=True, null=True)),
                ('elevator', models.BooleanField()),
                ('parking', models.BooleanField()),
                ('storage', models.BooleanField()),
                ('province', models.CharField(max_length=63)),
                ('city', models.CharField(max_length=63)),
                ('neighbourhood', models.CharField(max_length=63)),
                ('location', models.CharField(blank=True, max_length=1023, null=True)),
                ('photo_0', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_6', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_7', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_8', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_9', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.CharField(blank=True, max_length=30)),
                ('visible', models.BooleanField(default=True)),
                ('low_deposite', models.IntegerField()),
                ('low_rent', models.IntegerField()),
                ('high_deposite', models.IntegerField()),
                ('high_rent', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rentPosts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApartmentSell',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=63)),
                ('description', models.TextField(max_length=2047)),
                ('meterage', models.FloatField()),
                ('room', models.IntegerField()),
                ('build', models.IntegerField()),
                ('floor', models.IntegerField(blank=True, null=True)),
                ('total_floors', models.IntegerField(blank=True, null=True)),
                ('unit_per_floor', models.IntegerField(blank=True, null=True)),
                ('elevator', models.BooleanField()),
                ('parking', models.BooleanField()),
                ('storage', models.BooleanField()),
                ('province', models.CharField(max_length=63)),
                ('city', models.CharField(max_length=63)),
                ('neighbourhood', models.CharField(max_length=63)),
                ('location', models.CharField(blank=True, max_length=1023, null=True)),
                ('photo_0', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_1', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_2', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_3', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_4', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_5', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_6', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_7', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_8', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('photo_9', models.ImageField(blank=True, null=True, upload_to=posts.models.upload_to)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('timestamp', models.CharField(blank=True, max_length=30)),
                ('visible', models.BooleanField(default=True)),
                ('total_price', models.IntegerField()),
                ('price_per_meter', models.IntegerField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sellPosts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='PostSell',
        ),
    ]
