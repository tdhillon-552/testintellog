# Generated by Django 4.0.3 on 2022-03-28 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0003_alter_additionaldetails_form_delete_formtypes'),
    ]

    operations = [
        migrations.AddField(
            model_name='additionaldetails',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]