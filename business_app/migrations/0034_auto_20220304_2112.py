# Generated by Django 3.2.3 on 2022-03-04 15:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0033_auto_20220304_2101'),
    ]

    operations = [
        migrations.RenameField(
            model_name='backend_order',
            old_name='Number_of_Section',
            new_name='Backend_Price',
        ),
        migrations.RenameField(
            model_name='backend_order',
            old_name='files',
            new_name='Demo_project_File',
        ),
        migrations.RenameField(
            model_name='backend_order',
            old_name='Price',
            new_name='Number_Of_Section',
        ),
    ]