# Generated by Django 5.0.2 on 2024-02-14 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0010_imagess'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagess',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='imagen'),
        ),
        migrations.AlterField(
            model_name='imagess',
            name='title',
            field=models.CharField(max_length=200),
        ),
    ]
