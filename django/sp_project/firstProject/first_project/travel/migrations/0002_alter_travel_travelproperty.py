# Generated by Django 5.0.6 on 2024-07-05 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("travel", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="travel",
            name="travelProperty",
            field=models.TextField(),
        ),
    ]
