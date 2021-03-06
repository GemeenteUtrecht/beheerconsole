# Generated by Django 3.0.1 on 2020-02-03 16:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("processes", "0007_auto_20200120_1654"),
    ]

    operations = [
        migrations.CreateModel(
            name="StorageLocation",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="name")),
                (
                    "storage_type",
                    models.CharField(
                        choices=[("digital", "Digital"), ("analogue", "Analogue")],
                        default="digital",
                        max_length=50,
                        verbose_name="storage type",
                    ),
                ),
            ],
            options={
                "verbose_name": "storage location",
                "verbose_name_plural": "storage locations",
            },
        ),
        migrations.CreateModel(
            name="Storage",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "start",
                    models.DateField(
                        blank=True,
                        help_text="When did this become the primary storage?",
                        null=True,
                        verbose_name="start",
                    ),
                ),
                (
                    "end",
                    models.DateField(
                        blank=True,
                        help_text="When was this no longer the primary storage?",
                        null=True,
                        verbose_name="end",
                    ),
                ),
                (
                    "location_analogue",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"storage_type": "analogue"},
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="digital_storages",
                        to="processes.StorageLocation",
                        verbose_name="Location analogue",
                    ),
                ),
                (
                    "location_digital",
                    models.ForeignKey(
                        blank=True,
                        limit_choices_to={"storage_type": "digital"},
                        null=True,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="analogue_storages",
                        to="processes.StorageLocation",
                        verbose_name="Location digital",
                    ),
                ),
                (
                    "process",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="processes.Process",
                        verbose_name="process",
                    ),
                ),
            ],
            options={
                "verbose_name": "process storage",
                "verbose_name_plural": "process storages",
            },
        ),
    ]
