# Generated by Django 3.0.6 on 2020-05-11 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Promise_Of_the_Month', models.CharField(max_length=10000)),
                ('Promise_Of_the_Month_Proverb', models.CharField(max_length=100)),
                ('Promise_Of_the_day', models.CharField(max_length=10000)),
                ('Promise_Of_the_day_Proverb', models.CharField(max_length=100)),
                ('TODAY_WORD', models.CharField(max_length=200)),
                ('DAILY_THOUGHT', models.CharField(max_length=10000)),
            ],
        ),
    ]
