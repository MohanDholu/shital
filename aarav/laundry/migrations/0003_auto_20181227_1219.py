# Generated by Django 2.1.4 on 2018-12-27 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0002_auto_20181227_1204'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='order_status',
            field=models.CharField(default='Incoming', editable=False, max_length=20),
        ),
    ]
