# Generated by Django 5.1.3 on 2025-01-28 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veg', '0004_curries_fastfood_quickandeasy_starters_stirfry_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='curries',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='fastfood',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='quickandeasy',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='soups',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='starters',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='stirfry',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='vegbiryani',
            name='name',
            field=models.CharField(max_length=100),
        ),
    ]
