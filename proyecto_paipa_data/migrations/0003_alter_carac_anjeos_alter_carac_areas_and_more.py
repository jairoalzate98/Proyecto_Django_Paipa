# Generated by Django 4.2.1 on 2023-05-07 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto_paipa_data', '0002_rename_pare_baño_carac_pare_bano_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='carac',
            name='anjeos',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='carac',
            name='areas',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='carac',
            name='aseo',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='carac',
            name='barrio_vereda',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='carac',
            name='hacinami',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='carac',
            name='iluminacio',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='carac',
            name='municipios',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='carac',
            name='orden',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='carac',
            name='punt_sisb',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
        migrations.AlterField(
            model_name='carac',
            name='reci_basur',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='carac',
            name='reservorio',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='carac',
            name='ventilacio',
            field=models.CharField(max_length=100),
        ),
    ]