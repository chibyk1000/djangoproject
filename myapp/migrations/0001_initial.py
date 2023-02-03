# Generated by Django 4.1.5 on 2023-02-02 08:46

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                    "profile_pics",
                    models.ImageField(
                        blank=True, default="default.jpg", null=True, upload_to="user/"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Product",
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
                ("name", models.CharField(max_length=255, unique=True)),
                ("image", models.ImageField(upload_to="product_img")),
                ("price", models.FloatField()),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("P", "Phones & Tablets"),
                            ("C", "Clothings"),
                            ("E", "Electronics"),
                        ],
                        max_length=2,
                    ),
                ),
                (
                    "quantity_available",
                    models.IntegerField(blank=True, default="", null=True),
                ),
                ("description", ckeditor.fields.RichTextField()),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
