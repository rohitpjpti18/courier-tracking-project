# Generated by Django 2.2.2 on 2019-08-12 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='consignment',
            name='consignment_destination_pin_code',
            field=models.IntegerField(default=481001),
        ),
        migrations.AlterField(
            model_name='consignment',
            name='consignment_destination',
            field=models.CharField(choices=[('BGT', 'Balaghat (BGT)')], max_length=30),
        ),
        migrations.AlterField(
            model_name='consignment',
            name='consignment_source',
            field=models.CharField(choices=[('BGT', 'Balaghat (BGT)')], max_length=30),
        ),
    ]