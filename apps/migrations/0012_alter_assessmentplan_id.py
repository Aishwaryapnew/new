# Generated by Django 5.1.4 on 2024-12-16 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0011_alter_assessmentplan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentplan',
            name='id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
    ]
