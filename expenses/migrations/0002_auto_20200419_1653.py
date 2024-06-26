# Generated by Django 2.2.12 on 2020-04-19 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expense',
            name='body',
            field=models.TextField(max_length=255),
        ),
        migrations.AlterField(
            model_name='expense',
            name='category',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='expense',
            name='payment_method',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='expense',
            name='title',
            field=models.CharField(max_length=10),
        ),
    ]
