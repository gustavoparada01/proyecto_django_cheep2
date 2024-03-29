# Generated by Django 5.0.2 on 2024-02-18 00:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0017_contenido_alter_imagess_height_field'),
    ]

    operations = [
        migrations.CreateModel(
            name='CarouselImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='carousel_images/')),
                ('description', models.TextField()),
            ],
        ),
    ]
