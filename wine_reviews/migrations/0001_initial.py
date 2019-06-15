# Generated by Django 2.2.1 on 2019-06-15 04:50

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('designation', models.CharField(blank=True, max_length=255)),
                ('province', models.CharField(blank=True, max_length=255)),
                ('region_1', models.CharField(blank=True, max_length=60)),
                ('region_2', models.CharField(blank=True, max_length=60)),
                ('variety', models.CharField(blank=True, max_length=60)),
                ('winery', models.CharField(max_length=60)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6, null=True)),
                ('title', models.CharField(max_length=60)),
                ('taster_name', models.CharField(blank=True, max_length=60)),
                ('taster_twitter_handle', models.CharField(blank=True, max_length=30)),
                ('points', models.PositiveSmallIntegerField(validators=[django.core.validators.MaxValueValidator(100)])),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='wine_reviews.Country')),
            ],
        ),
    ]
