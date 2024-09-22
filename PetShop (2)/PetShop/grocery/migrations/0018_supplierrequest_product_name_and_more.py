# Generated by Django 5.0.4 on 2024-05-02 14:19

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0017_adminrequest_description_adminrequest_product_name_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='supplierrequest',
            name='product_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='adminrequest',
            name='product_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='adminrequest',
            name='requested_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]