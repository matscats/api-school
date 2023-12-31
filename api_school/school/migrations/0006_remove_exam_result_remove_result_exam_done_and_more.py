# Generated by Django 5.0 on 2023-12-08 00:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0005_remove_result_exam_remove_result_user_exam_result_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exam',
            name='result',
        ),
        migrations.RemoveField(
            model_name='result',
            name='exam_done',
        ),
        migrations.AddField(
            model_name='exam',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='result',
            name='exam',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.exam'),
        ),
    ]
