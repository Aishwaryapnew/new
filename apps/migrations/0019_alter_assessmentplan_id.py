# Generated by Django 5.1.4 on 2024-12-17 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0018_alter_assessmentplan_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentplan',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
