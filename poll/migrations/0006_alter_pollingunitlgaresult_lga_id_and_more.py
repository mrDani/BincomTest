# Generated by Django 4.0.4 on 2022-05-10 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0005_rename_polling_unit_id_pollingunitlgaresult_total_lga_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pollingunitlgaresult',
            name='lga_id',
            field=models.IntegerField(unique=True),
        ),
        migrations.AlterField(
            model_name='pollingunitlgaresult',
            name='lga_name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
