# Generated by Django 4.2.5 on 2024-01-18 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('cId', models.IntegerField(primary_key=True, serialize=False)),
                ('courseName', models.CharField(max_length=255)),
                ('teacher', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('sId', models.IntegerField(primary_key=True, serialize=False)),
                ('sName', models.CharField(max_length=255)),
                ('contactNo', models.CharField(max_length=15)),
                ('Address', models.TextField()),
                
            ],
        ),
        migrations.CreateModel(
            name='StudentCourse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sId', models.IntegerField()),
                ('cId', models.IntegerField()),
                ('ct1', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ct2', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ct3', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('tId', models.IntegerField(primary_key=True, serialize=False)),
                ('tName', models.CharField(max_length=255)),
                ('contactNo', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]