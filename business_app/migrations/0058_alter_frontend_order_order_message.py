# Generated by Django 3.2.3 on 2022-03-13 08:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0057_alter_frontend_order_order_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontend_order',
            name='order_message',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='business_app.message_manu'),
        ),
    ]
