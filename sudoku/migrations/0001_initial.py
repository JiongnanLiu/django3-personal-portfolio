# Generated by Django 3.1 on 2020-10-27 19:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sudoku',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('profilePic', models.ImageField(upload_to='sudoku/images/')),
                ('time', models.TimeField()),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
    ]
