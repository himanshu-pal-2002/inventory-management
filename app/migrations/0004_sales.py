# Generated by Django 4.0.6 on 2022-08-06 04:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_purchase'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sales',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.FloatField()),
                ('price', models.FloatField()),
                ('total_amt', models.FloatField()),
                ('sale_date', models.DateTimeField(auto_now_add=True)),
                ('customer_name', models.CharField(blank=True, max_length=50)),
                ('customer_mobile', models.CharField(max_length=50)),
                ('customer_address', models.TextField()),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
            ],
            options={
                'verbose_name_plural': 'Sales',
            },
        ),
    ]
