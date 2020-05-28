# Generated by Django 3.0.6 on 2020-05-10 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin1', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='permanent_reg',
            name='user_type',
            field=models.CharField(choices=[('DONATION', 'DONATION'), ('SUBSCRIBER', 'SUBSCRIBER'), ('BUYER', 'BUYER')], max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='temp_reg',
            name='user_type',
            field=models.CharField(blank=True, choices=[('DONATION', 'DONATION'), ('SUBSCRIBER', 'SUBSCRIBER'), ('BUYER', 'BUYER')], max_length=40),
        ),
        migrations.AlterField(
            model_name='permanent_reg',
            name='full_add',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='temp_reg',
            name='full_add',
            field=models.TextField(max_length=500),
        ),
    ]
