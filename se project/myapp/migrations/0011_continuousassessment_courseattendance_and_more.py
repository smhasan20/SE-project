# Generated by Django 4.2.5 on 2024-01-30 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_studentcourse_comment_alter_student_password_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContinuousAssessment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.DecimalField(decimal_places=2, max_digits=5)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
            ],
        ),
        migrations.CreateModel(
            name='CourseAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attendance', models.CharField(default='0%', max_length=5)),
                ('comment', models.TextField(default=' ')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.course')),
            ],
        ),
        migrations.AddField(
            model_name='teacher',
            name='password',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AlterField(
            model_name='student',
            name='password',
            field=models.CharField(default='', max_length=15),
        ),
        migrations.DeleteModel(
            name='StudentCourse',
        ),
        migrations.AddField(
            model_name='courseattendance',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student'),
        ),
        migrations.AddField(
            model_name='continuousassessment',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.student'),
        ),
    ]
