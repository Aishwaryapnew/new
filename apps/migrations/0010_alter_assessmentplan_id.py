# Generated by Django 5.1.4 on 2024-12-16 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0009_rename_uid_assessmentplan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentplan',
            name='id',
            field=models.Field(primary_key=True, serialize=False),
        ),
    ]