# Generated by Django 5.0.2 on 2024-02-14 23:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0013_remove_imagess_pedido_calzadoss_imagess'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagess',
            name='title',
            field=models.CharField(default=1, max_length=180),
            preserve_default=False,
        ),
    ]
