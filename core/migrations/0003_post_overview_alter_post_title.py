# Generated by Django 4.2.7 on 2023-11-08 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_category_alter_post_timestamp_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='overview',
            field=models.CharField(blank=True, max_length=60, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=30),
        ),
    ]