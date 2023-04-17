# Generated by Django 4.2 on 2023-04-08 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("user_name", models.CharField(max_length=200)),
                ("user_birth", models.DateField()),
                (
                    "user_gender",
                    models.CharField(
                        choices=[
                            ("M", "Male"),
                            ("F", "Female"),
                            ("O", "Other"),
                            ("P", "Prefer not to answer"),
                        ],
                        max_length=1,
                    ),
                ),
            ],
        ),
    ]