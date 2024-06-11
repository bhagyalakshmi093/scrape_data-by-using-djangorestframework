# Generated by Django 5.0.6 on 2024-06-10 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='OfficialLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='CryptoData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coin', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('price_change', models.FloatField()),
                ('market_cap', models.BigIntegerField()),
                ('market_cap_rank', models.IntegerField()),
                ('volume', models.BigIntegerField()),
                ('volume_rank', models.IntegerField()),
                ('volume_change', models.FloatField()),
                ('circulating_supply', models.BigIntegerField()),
                ('total_supply', models.BigIntegerField()),
                ('diluted_market_cap', models.BigIntegerField()),
                ('contracts', models.ManyToManyField(to='crypto.contract')),
                ('official_links', models.ManyToManyField(to='crypto.officiallink')),
                ('socials', models.ManyToManyField(to='crypto.social')),
            ],
        ),
    ]
