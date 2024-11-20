# Generated by Django 4.1.3 on 2024-11-19 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_alter_profile_travel_preferences'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='budget_range',
            field=models.CharField(blank=True, default='', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='favorite_destinations',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='interests',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='languages_spoken',
            field=models.CharField(blank=True, default='', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, default='', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='travel_preferences',
            field=models.CharField(blank=True, default='', max_length=350, null=True),
        ),
    ]
