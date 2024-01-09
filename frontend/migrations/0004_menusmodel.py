# Generated by Django 4.2.1 on 2023-10-23 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0003_alter_slider_is_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenusModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('link', models.CharField(blank=True, max_length=250, null=True)),
                ('has_children', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
    ]
