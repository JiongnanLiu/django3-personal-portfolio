# Generated by Django 3.1 on 2020-11-08 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sudoku', '0002_ranking'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranking',
            name='time',
            field=models.DurationField(),
        ),
    ]