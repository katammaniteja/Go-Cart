# Generated by Django 3.2.9 on 2021-12-25 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20211225_1222'),
    ]

    operations = [
        migrations.AlterField(
            model_name='categories',
            name='meta_description',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='categories',
            name='meta_title',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='products',
            name='meta_description',
            field=models.CharField(max_length=150),
        ),
        migrations.AlterField(
            model_name='products',
            name='meta_title',
            field=models.CharField(max_length=150),
        ),
    ]