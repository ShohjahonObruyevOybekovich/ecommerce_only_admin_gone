# Generated by Django 5.1.1 on 2024-10-03 17:20

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('body', '0010_alter_liked_uuid_alter_savatcha_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liked',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('78809998-1c82-42ed-9080-67fa017f64c6'), editable=False, unique=True),
        ),
        migrations.AlterField(
            model_name='savatcha',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('2f0c24b7-ce5c-4d29-9a48-a007df0e02f1'), editable=False, unique=True),
        ),
    ]
