# Generated by Django 3.2.3 on 2022-03-08 20:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business_app', '0041_auto_20220304_2158'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontend_order',
            name='mNU',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]