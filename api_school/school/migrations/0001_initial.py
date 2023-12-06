# Generated by Django 5.0 on 2023-12-06 19:12

import django.contrib.postgres.fields
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=20)),
                ('topic', models.CharField(max_length=80)),
                ('title', models.TextField()),
                ('answer', models.CharField(max_length=500)),
                ('alternatives', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=500), size=5)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('cpf', models.CharField(max_length=11)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_student', models.BooleanField(default=False)),
                ('is_teacher', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questions', models.ManyToManyField(to='school.question')),
                ('users', models.ManyToManyField(to='school.user')),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField(validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.exam')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school.user')),
            ],
        ),
        migrations.CreateModel(
            name='VirtualClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', models.PositiveSmallIntegerField()),
                ('letter', models.CharField(max_length=1)),
                ('teacher', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='school.user')),
            ],
        ),
    ]
