# Generated by Django 5.1.7 on 2025-04-06 22:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_interesse_cliente'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='quantidade',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
