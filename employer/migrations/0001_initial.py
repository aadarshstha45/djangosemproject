# Generated by Django 4.2 on 2023-07-20 07:14

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                (
                    "company_name",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "company_website",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "company_location",
                    models.CharField(blank=True, max_length=255, null=True),
                ),
                (
                    "logo",
                    models.FileField(
                        blank=True,
                        null=True,
                        upload_to="logo/",
                        validators=[
                            django.core.validators.FileExtensionValidator(
                                allowed_extensions=["png", "jpg", "jpeg"]
                            )
                        ],
                    ),
                ),
            ],
        ),
    ]
