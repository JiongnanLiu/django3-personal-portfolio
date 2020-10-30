# Generated by Django 3.1 on 2020-10-29 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockscreener', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=4)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('volume', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='stockscreener',
            name='email',
            field=models.EmailField(db_column='email', default=None, max_length=256, unique=True),
        ),
    ]
