# Generated by Django 5.0.4 on 2024-05-14 08:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0006_savatcha_product_amount_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='liked',
            name='liked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddConstraint(
            model_name='liked',
            constraint=models.UniqueConstraint(fields=('user', 'product'), name='unique_liked_product'),
        ),
    ]
