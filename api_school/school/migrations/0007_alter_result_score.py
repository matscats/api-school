# Generated by Django 5.0 on 2023-12-08 00:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0006_remove_exam_result_remove_result_exam_done_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='score',
            field=models.IntegerField(null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)]),
        ),
    ]
