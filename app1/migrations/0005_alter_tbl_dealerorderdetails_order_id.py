# Generated by Django 4.0 on 2022-05-28 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0004_tbl_idgen_orid_tbl_idgen_p1id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_dealerorderdetails',
            name='order_id',
            field=models.CharField(max_length=30),
        ),
    ]
