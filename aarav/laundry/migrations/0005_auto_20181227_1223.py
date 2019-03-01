# Generated by Django 2.1.4 on 2018-12-27 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0004_auto_20181227_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='cloth_quantity',
            field=models.IntegerField(default=0, editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='customerorder',
            name='total_bill',
            field=models.FloatField(default=0, editable=False, null=True),
        ),
    ]
