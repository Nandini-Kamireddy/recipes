# Generated by Django 5.1.3 on 2025-02-04 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('veg', '0006_soups_video'),
    ]

    operations = [
        migrations.AddField(
            model_name='curries',
            name='video',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='fastfood',
            name='video',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='quickandeasy',
            name='video',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='starters',
            name='video',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='stirfry',
            name='video',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='vegbiryani',
            name='video',
            field=models.URLField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='soups',
            name='video',
            field=models.URLField(max_length=500, null=True),
        ),
    ]
