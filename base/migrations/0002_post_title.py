# Generated by Django 5.0.2 on 2024-02-09 00:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Title',
            field=models.TextField(default='Titulo', max_length=200),
            preserve_default=False,
        ),
    ]
