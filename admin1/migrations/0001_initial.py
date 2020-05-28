# Generated by Django 3.0.6 on 2020-05-10 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='permanent_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('building_name', models.CharField(max_length=100)),
                ('Area_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('full_add', models.CharField(max_length=400)),
                ('pincode', models.CharField(max_length=6)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='temp_reg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('phone_number', models.CharField(max_length=10)),
                ('building_name', models.CharField(max_length=100)),
                ('Area_name', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('full_add', models.CharField(max_length=400)),
                ('pincode', models.CharField(max_length=6)),
                ('start_date', models.DateTimeField(auto_now_add=True)),
                ('end_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
