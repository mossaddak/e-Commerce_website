# Generated by Django 3.2.3 on 2022-03-08 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0044_message_manu'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontend_order',
            name='order_message',
            field=models.ManyToManyField(to='business_app.Message_Manu'),
        ),
    ]