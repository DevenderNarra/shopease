# Generated by Django 4.2.16 on 2024-12-08 10:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0009_rename_paid_by_payment_customer"),
    ]

    operations = [
        migrations.AlterField(
            model_name="payment",
            name="customer",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="shop.user"
            ),
        ),
    ]
