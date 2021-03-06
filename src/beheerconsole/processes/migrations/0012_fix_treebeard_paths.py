# Generated by Django 3.0.3 on 2020-02-25 15:56

from django.db import migrations


def fix_treebeard_paths(apps, _):
    Department = apps.get_model("processes", "Department")

    for index, dep in enumerate(Department.objects.all(), start=1):
        dep.path = f"{index:04d}"
        dep.save()


class Migration(migrations.Migration):

    dependencies = [
        ("processes", "0011_auto_20200225_1537"),
    ]

    operations = [
        migrations.RunPython(fix_treebeard_paths, migrations.RunPython.noop),
    ]
