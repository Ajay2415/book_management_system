# Generated by Django 5.0.7 on 2024-07-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("bookapp", "0002_alter_bookmodel_book_img"),
    ]

    operations = [
        migrations.AlterField(
            model_name="bookmodel",
            name="book_img",
            field=models.ImageField(upload_to="static/books/"),
        ),
    ]