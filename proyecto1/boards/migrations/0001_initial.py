# Generated by Django 4.2.2 on 2023-06-24 15:21

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Author",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                (
                    "title",
                    models.CharField(
                        choices=[("MR", "Mr."), ("MRS", "Mrs."), ("MS", "Ms.")],
                        max_length=3,
                    ),
                ),
                ("birth_date", models.DateField(blank=True, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name="Book",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("authors", models.ManyToManyField(to="boards.author")),
            ],
        ),
    ]