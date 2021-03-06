# Generated by Django 4.0.5 on 2022-06-17 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_rename_product_id_tbl_dealerorderdetails_prod_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbl_idgen',
            name='dlid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='tbl_delivery',
            fields=[
                ('delivery_id', models.CharField(max_length=30, primary_key=True, serialize=False)),
                ('status', models.CharField(max_length=30)),
                ('date', models.CharField(max_length=30)),
                ('time', models.CharField(max_length=30)),
                ('dealer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.dealer')),
                ('order_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.dealerorder')),
            ],
            options={
                'db_table': 'tbl_delivery',
            },
        ),
    ]
