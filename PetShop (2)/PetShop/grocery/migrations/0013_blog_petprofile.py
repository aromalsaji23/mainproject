# Generated by Django 5.0.1 on 2024-01-31 13:57

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0012_auto_20210510_1528'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('content', models.TextField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PetProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('breed', models.CharField(max_length=100, null=True)),
                ('age', models.PositiveIntegerField(max_length=100, null=True)),
                ('image', models.FileField(null=True, upload_to='')),
                ('veterinarian', models.CharField(max_length=100, null=True)),
                ('visit_date', models.DateField(null=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owned_pets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]