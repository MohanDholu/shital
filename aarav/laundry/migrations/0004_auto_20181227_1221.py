# Generated by Django 2.1.4 on 2018-12-27 12:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('laundry', '0003_auto_20181227_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerorder',
            name='total_bill',
            field=models.FloatField(editable=False, null=True),
        ),
    ]
