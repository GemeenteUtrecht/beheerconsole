# Generated by Django 3.0.1 on 2020-01-16 10:11

from django.db import migrations


def populate_name(apps, _):
    Process = apps.get_model("processes.Process")
    for process in Process.objects.filter(name=""):
        process.name = process.camunda_id
        process.save()


class Migration(migrations.Migration):

    dependencies = [
        ('processes', '0004_process_name'),
    ]

    operations = [
        migrations.RunPython(populate_name, migrations.RunPython.noop),
    ]