# Generated by Django 4.1.7 on 2023-03-20 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0002_rename_enter_details_enter_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='enter_detail',
            name='acceleration',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='enter_detail',
            name='cylinders',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='enter_detail',
            name='displacement',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='enter_detail',
            name='horsepower',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='enter_detail',
            name='model',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='enter_detail',
            name='origin',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='enter_detail',
            name='weight',
            field=models.IntegerField(),
        ),
    ]
