# Generated by Django 4.2.16 on 2024-12-06 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="order",
        ),
        migrations.AddField(
            model_name="order",
            name="payment",
            field=models.OneToOneField(
                default=234,
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.payment",
            ),
            preserve_default=False,
        ),
    ]