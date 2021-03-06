# Generated by Django 3.0.4 on 2020-03-30 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chemicals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc_chemical', models.CharField(max_length=100)),
                ('class_of_drugs', models.CharField(max_length=100)),
                ('dose', models.IntegerField()),
                ('dose_one', models.IntegerField()),
                ('purchase_price', models.IntegerField()),
                ('remaining_medicine', models.IntegerField()),
            ],
            options={
                'db_table': 'chemicals',
            },
        ),
    ]
