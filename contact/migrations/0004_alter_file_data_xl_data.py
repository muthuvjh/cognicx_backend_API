# Generated by Django 4.1.4 on 2023-01-03 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_rename_contact_status_file_data_campaign_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='file_data',
            name='xl_data',
            field=models.JSONField(default={}),
        ),
    ]