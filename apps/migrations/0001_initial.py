# Generated by Django 5.1.4 on 2024-12-12 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AssessmentPlan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('duration', models.CharField(max_length=255)),
                ('Weightage', models.CharField(max_length=255)),
                ('typeology', models.CharField(max_length=255)),
                ('Pattern', models.CharField(max_length=255)),
                ('schedule', models.CharField(max_length=255)),
                ('topicsovered', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'project',
            },
        ),
    ]
