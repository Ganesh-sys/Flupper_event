# Generated by Django 3.1.7 on 2021-03-22 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FlupperApp', '0002_auto_20210320_0719'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category_details',
            name='event_image',
            field=models.ImageField(blank=True, null=True, upload_to='Files/'),
        ),
    ]
