# Generated by Django 4.0.6 on 2022-10-08 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_inventory_sales_alter_inventory_pur_qty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchase',
            name='total_amt',
            field=models.FloatField(default=0, editable=False),
        ),
    ]