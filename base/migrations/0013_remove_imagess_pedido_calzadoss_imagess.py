# Generated by Django 5.0.2 on 2024-02-14 22:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_remove_imagess_title_imagess_pedido'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagess',
            name='pedido',
        ),
        migrations.AddField(
            model_name='calzadoss',
            name='imagess',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='imagen', to='base.imagess'),
            preserve_default=False,
        ),
    ]
