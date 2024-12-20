# Generated by Django 4.2.16 on 2024-12-07 19:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0002_remove_payment_order_order_payment"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="payment",
            name="created_at",
        ),
        migrations.AddField(
            model_name="payment",
            name="paid_by",
            field=models.OneToOneField(
                default="unknown",
                on_delete=django.db.models.deletion.CASCADE,
                to="shop.user",
            ),
        ),
    ]
