# Generated by Django 4.0.1 on 2024-08-08 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sno', models.IntegerField()),
                ('sname', models.CharField(max_length=64)),
                ('ssalary', models.FloatField()),
                ('ssddress', models.CharField(max_length=64)),
            ],
        ),
    ]
