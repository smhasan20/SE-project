# Generated by Django 4.2.5 on 2024-01-27 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_alter_student_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default='pbkdf2_sha256$600000$iwbB9gHeEhvKYSyT0m7kyY$Am/JQPb6IsASjfc09VC6q8pC9LSAOQa87+4yl4EbZ0Y=', max_length=12),
        ),
    ]
