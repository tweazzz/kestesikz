# Generated by Django 4.2.7 on 2023-12-26 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_jobhistory_end_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobhistory',
            name='end_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='jobhistory',
            name='start_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='specialityhistory',
            name='end_date',
            field=models.DateField(),
        ),
    ]
