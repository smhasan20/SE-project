# Generated by Django 4.2.5 on 2024-01-28 13:40

import contextlib
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0009_studentcourse_attendance_alter_student_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcourse',
            name='comment',
            field=models.TextField(default=contextlib.nullcontext),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$OE6orBHlF714ixNNbWAimc$d+iFTOSKes9CjjtdBluhqzfZnNPRJCFigp5CNJ/HuMo=', max_length=12),
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='attendance',
            field=models.CharField(default='0%', max_length=5),
        ),
    ]
