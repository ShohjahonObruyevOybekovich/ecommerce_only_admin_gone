# Generated by Django 5.0.4 on 2024-05-10 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0003_remove_product_photo_or_video_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='media/product_media/')),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='photos_or_videos',
        ),
        migrations.AddField(
            model_name='product',
            name='photos_or_videos',
            field=models.ManyToManyField(related_name='products', to='body.productmedia'),
        ),
    ]
