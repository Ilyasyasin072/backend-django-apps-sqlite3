# Generated by Django 3.0.4 on 2020-04-02 03:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('doctor', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScheduleDoctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('detail_schedule', models.CharField(max_length=100)),
                ('id_doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='doctor.Doctor')),
            ],
            options={
                'db_table': 'schedule_doctor',
            },
        ),
    ]
