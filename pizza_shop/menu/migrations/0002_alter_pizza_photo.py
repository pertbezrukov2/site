# Generated by Django 5.1.4 on 2025-01-08 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pizza',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='pizza_images/'),
        ),
    ]
