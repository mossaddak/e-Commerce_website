# Generated by Django 3.2.3 on 2022-03-04 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0035_rename_demo_project_file_backend_order_project_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='backend_order',
            name='Project_File',
            field=models.FileField(blank=True, null=True, upload_to='backend_file/'),
        ),
    ]
