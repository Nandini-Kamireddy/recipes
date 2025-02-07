# Generated by Django 5.1.3 on 2025-01-26 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coffee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ingredients', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='media/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Juices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ingredients', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='media/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Milkshakes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ingredients', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='media/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Smoothies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ingredients', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='media/')),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('ingredients', models.TextField()),
                ('image', models.ImageField(null=True, upload_to='media/')),
                ('description', models.TextField()),
            ],
        ),
    ]
