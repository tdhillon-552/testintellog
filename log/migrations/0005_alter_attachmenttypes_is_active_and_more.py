# Generated by Django 4.0.3 on 2022-03-30 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0004_additionaldetails_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachmenttypes',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='customfields',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='entityrecordtypes',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='inputtypes',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='masterrecords',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='masterrecordtypes',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='persontypes',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='vehicletypes',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
