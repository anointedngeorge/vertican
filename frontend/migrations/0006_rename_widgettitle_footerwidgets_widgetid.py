# Generated by Django 4.2.9 on 2024-01-23 07:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_footerwidgets'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footerwidgets',
            old_name='widgetTitle',
            new_name='widgetID',
        ),
    ]
