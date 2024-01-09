# Generated by Django 4.2.1 on 2023-09-23 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('matrixpro', '0013_remove_propertysalesmodel_discount_currency_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertysalesmodel',
            name='pro_price_currency',
        ),
        migrations.AlterField(
            model_name='propertysalesmodel',
            name='pro_price',
            field=models.FloatField(blank=True, max_length=500, null=True),
        ),
    ]
