# Generated by Django 4.1.5 on 2023-02-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0006_alter_suggestquestion_lastname"),
    ]

    operations = [
        migrations.AlterField(
            model_name="suggestquestion",
            name="lastName",
            field=models.CharField(max_length=10),
        ),
    ]
