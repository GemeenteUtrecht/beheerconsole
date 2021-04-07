# Generated by Django 3.0.1 on 2020-02-25 13:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("processes", "0009_merge_20200225_1353"),
    ]

    operations = [
        migrations.AddField(
            model_name="process",
            name="location_analogue",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"storage_type": "analogue"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="processes.StorageLocation",
                verbose_name="Location analogue",
            ),
        ),
        migrations.AddField(
            model_name="process",
            name="location_digital",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"storage_type": "digital"},
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                related_name="+",
                to="processes.StorageLocation",
                verbose_name="Location digital",
            ),
        ),
        migrations.DeleteModel(
            name="Storage",
        ),
    ]
