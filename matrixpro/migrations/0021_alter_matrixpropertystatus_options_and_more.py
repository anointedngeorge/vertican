# Generated by Django 4.2.1 on 2023-09-28 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('matrixpro', '0020_alter_matrixproperty_property_desc_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='matrixpropertystatus',
            options={'verbose_name': 'Property Status', 'verbose_name_plural': 'Property Status'},
        ),
        migrations.AlterField(
            model_name='matrixproperty',
            name='status',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='matrixpro.matrixpropertystatus'),
        ),
    ]