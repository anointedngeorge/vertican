# Generated by Django 4.2.1 on 2023-09-29 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixpro', '0022_matrixpropertytype_short_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='matrixpropertytype',
            name='index',
            field=models.IntegerField(default=0),
        ),
    ]
