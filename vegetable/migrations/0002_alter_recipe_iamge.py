# Generated by Django 4.2.5 on 2023-10-03 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vegetable', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='iamge',
            field=models.ImageField(null=True, upload_to='recipe'),
        ),
    ]
