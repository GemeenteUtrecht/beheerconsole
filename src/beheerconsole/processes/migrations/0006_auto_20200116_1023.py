# Generated by Django 3.0.1 on 2020-01-16 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("processes", "0005_auto_20200116_1011"),
    ]

    operations = [
        migrations.AlterField(
            model_name="process",
            name="camunda_id",
            field=models.CharField(
                blank=True,
                help_text="Process definition ID in Camunda.",
                max_length=255,
                verbose_name="Camunda process",
            ),
        ),
    ]
