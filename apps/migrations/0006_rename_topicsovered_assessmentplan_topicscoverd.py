# Generated by Django 5.1.4 on 2024-12-16 05:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_alter_assessmentplan_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assessmentplan',
            old_name='topicsovered',
            new_name='topicscoverd',
        ),
    ]