# Generated by Django 4.2 on 2023-07-29 08:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0004_remove_job_company_name_remove_job_company_website_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="job",
            name="company_name",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="job",
            name="company_website",
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name="job",
            name="location",
            field=models.CharField(blank=True, max_length=201, null=True),
        ),
        migrations.AddField(
            model_name="job",
            name="logo",
            field=models.FileField(
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
    ]