# Generated by Django 5.1.2 on 2024-10-16 03:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BlogPost",
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
                ("title", models.CharField(max_length=120)),
                ("content", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="blogs/")),
                ("timestamp", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
