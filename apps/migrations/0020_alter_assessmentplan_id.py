# Generated by Django 5.1.4 on 2024-12-17 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0019_alter_assessmentplan_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assessmentplan',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]